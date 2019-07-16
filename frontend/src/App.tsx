import React from "react";
import "./App.css";
import { TinyKafkaClient } from "./generated/proto/api_pb_service";
import { WatchRequest, WatchResponse } from "./generated/proto/api_pb";

const HOST = "http://127.0.0.1:8080";
const client = new TinyKafkaClient(HOST);

class App extends React.Component<{}, { messages: String[] }> {
  constructor(props: any) {
    super(props);

    this.state = {
      messages: []
    };
  }

  componentDidMount() {
    const stream = client.watch(new WatchRequest());
    stream.on("data", (response: WatchResponse) => {
      this.setState({
        messages: [...this.state.messages, response.getMessage()]
      });
    });
  }

  public render() {
    return (
      <div className="App">
        <header className="App-header">
          {this.state.messages.map(message => {
            return <div>{message}</div>;
          })}
        </header>
      </div>
    );
  }
}

export default App;

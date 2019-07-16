import time
from concurrent.futures import ThreadPoolExecutor

import grpc
import zmq

from proto.api_pb2_grpc import add_TinyKafkaServicer_to_server
from proto.api_pb2_grpc import TinyKafkaServicer
from proto.api_pb2 import SendMessageRequest
from proto.api_pb2 import SendMessageResponse
from proto.api_pb2 import WatchResponse


TOPIC = "messages"
PORT = "8088"
BIND = f"tcp://127.0.0.1:{PORT}"


class TinyKafkaImpl(TinyKafkaServicer):
    def __init__(self):
        self.ctx = zmq.Context()
        self._send_sock = self.ctx.socket(zmq.PUB)
        self._send_sock.bind(BIND)

    def SendMessage(self, request: SendMessageRequest, context):
        msg = request.message
        self._send_sock.send_string(f"{TOPIC} {msg}")
        print(f"message received: {msg}")
        return SendMessageResponse()

    def Watch(self, request, context):
        sock = self.ctx.socket(zmq.SUB)
        sock.setsockopt_string(zmq.SUBSCRIBE, TOPIC)
        sock.connect(BIND)

        while True:
            resp = sock.recv_string()
            _, message = resp.split(" ", 1)
            yield WatchResponse(message=message)


if __name__ == "__main__":
    executor = ThreadPoolExecutor(max_workers=100)
    server = grpc.server(executor)
    add_TinyKafkaServicer_to_server(TinyKafkaImpl(), server)
    server.add_insecure_port("127.0.0.1:50051")
    server.start()
    print("Running server on port 50051")

    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            break

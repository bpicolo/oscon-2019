FROM golang:alpine as builder
RUN apk --no-cache add git
RUN go get -u github.com/improbable-eng/grpc-web/go/grpcwebproxy

FROM alpine
RUN apk --no-cache add ca-certificates
WORKDIR /
COPY --from=builder /go/bin/grpcwebproxy .
CMD ["/grpcwebproxy", "--backend_addr", "host.docker.internal:50051", "--server_http_max_read_timeout", "86400s", "--server_http_max_write_timeout", "86400s", "--run_tls_server=false", "--backend_tls=false", "--allowed_origins", "http://localhost:3000"]

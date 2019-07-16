import grpc
from proto.api_pb2_grpc import TinyKafkaStub


def get_client():
    return TinyKafkaStub(grpc.insecure_channel("127.0.0.1:50051"))

import asyncio
from concurrent import futures
import grpc

# Подключение рефлексии
from grpc_reflection.v1alpha import reflection

from config import settings
# Импорты контракта и сервиса
from contracts.services.payments import payments_service_pb2
from contracts.services.payments import payments_service_pb2_grpc
from libs.grpc.server.base import build_grpc_server
from services.payments.apps.payments.api.grpc import PaymentsMockService

# Логгер и интерцепторы
from libs.logger import get_logger
from libs.grpc.server.interceptors.logger_interceptor import GRPCLoggerInterceptor
from libs.grpc.server.interceptors.exception_interceptor import GRPCExceptionInterceptor

async def serve():
    logger = get_logger("MOCK_SERVICE_GRPC_SERVER")
    server = build_grpc_server(settings.mock_grpc_server, logger)

    payments_service_pb2_grpc.add_PaymentsServiceServicer_to_server(PaymentsMockService(), server)

    reflection.enable_server_reflection(
        (
            reflection.SERVICE_NAME,
            payments_service_pb2.DESCRIPTOR.services_by_name['PaymentsService'].full_name
        ),
        server
    )

    await server.start()
    await server.wait_for_termination()


if __name__ == '__main__':
    asyncio.run(serve())

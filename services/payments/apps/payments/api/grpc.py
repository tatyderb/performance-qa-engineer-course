from grpc.aio import ServicerContext

from contracts.services.payments.payments_service_pb2_grpc import PaymentsServiceServicer
from contracts.services.payments.rpc_authorize_payment_pb2 import (
    AuthorizePaymentRequest,
    AuthorizePaymentResponse
)
from contracts.services.payments.rpc_capture_payment_pb2 import (
    CapturePaymentRequest,
    CapturePaymentResponse
)
from contracts.services.payments.rpc_refund_payment_pb2 import (
    RefundPaymentRequest,
    RefundPaymentResponse
)

# Импортируем ранее созданный загрузчик моков
from services.payments.apps.payments.api.mock import loader


class PaymentsMockService(PaymentsServiceServicer):
    async def RefundPayment(self, request: RefundPaymentRequest, context: ServicerContext) -> RefundPaymentResponse:
        return await loader.load_grpc_with_timeout("RefundPayment/default.json", RefundPaymentResponse)

    async def CapturePayment(self, request: CapturePaymentRequest, context: ServicerContext) -> CapturePaymentResponse:
        return await loader.load_grpc_with_timeout("CapturePayment/default.json", CapturePaymentResponse)

    async def AuthorizePayment(self, request: AuthorizePaymentRequest, context: ServicerContext) -> AuthorizePaymentResponse:
        return await loader.load_grpc_with_timeout("AuthorizePayment/default.json", AuthorizePaymentResponse)


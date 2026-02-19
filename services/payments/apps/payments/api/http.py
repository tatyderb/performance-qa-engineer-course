from fastapi import APIRouter  # FastAPI router для группировки маршрутов

# Базовые маршруты (Enum с путями, например "/api/v1/payments")
from libs.routes import APIRoutes
# Импортируем ранее созданный загрузчик моков
from services.payments.apps.payments.api.mock import loader
# Импортируем схемы запроса и ответа из контракта
from services.payments.apps.payments.schema.payments import (
    RefundPaymentRequestSchema,
    RefundPaymentResponseSchema,
    CapturePaymentRequestSchema,
    CapturePaymentResponseSchema,
    AuthorizePaymentRequestSchema,
    AuthorizePaymentResponseSchema
)

# Создаём отдельный router для payments mock-сервиса
payments_mock_router = APIRouter(
    prefix=APIRoutes.PAYMENTS,  # "/api/v1/payments"
    tags=[APIRoutes.PAYMENTS.as_tag()]  # Для Swagger-документации
)


# ============================
# Эндпоинт: /refund-payment
# ============================
@payments_mock_router.post('/refund-payment', response_model=RefundPaymentResponseSchema)
async def refund_payment_view(request: RefundPaymentRequestSchema):
    """
    Обрабатывает запрос возврата платежа.
    Загружает мок из JSON-файла и возвращает как ответ.
    """
    return await loader.load_http_with_timeout(
        "refund_payment/default.json",  # путь к JSON-файлу с ответом
        RefundPaymentResponseSchema  # схема ответа
    )


# ============================
# Эндпоинт: /capture-payment
# ============================
@payments_mock_router.post('/capture-payment', response_model=CapturePaymentResponseSchema)
async def capture_payment_view(request: CapturePaymentRequestSchema):
    """
    Обрабатывает запрос на подтверждение платежа.
    """
    return await loader.load_http_with_timeout(
        "capture_payment/default.json",
        CapturePaymentResponseSchema
    )


# ============================
# Эндпоинт: /authorize-payment
# ============================
@payments_mock_router.post('/authorize-payment', response_model=AuthorizePaymentResponseSchema)
async def authorize_payment_view(request: AuthorizePaymentRequestSchema):
    """
    Обрабатывает запрос авторизации платежа по карте.
    """
    return await loader.load_http_with_timeout(
        "authorize_payment/default.json",
        AuthorizePaymentResponseSchema
    )

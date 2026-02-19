import uvicorn
from fastapi import FastAPI

# Импортируем роутер, реализующий HTTP мок-эндпоинты
from services.payments.apps.payments.api.http import payments_mock_router

# Создаём FastAPI-приложение с названием (отображается в Swagger UI)
app = FastAPI(title="payments-service")

# Подключаем наш моковый роутер с endpoint-ами
app.include_router(payments_mock_router)

# Точка входа при запуске из консоли: python -m services.payments.server.http
if __name__ == "__main__":
    import sys
    workers = 3 if not sys.platform.startswith('win') else 1
    print(f"{workers=}")
    uvicorn.run(
        app="services.payments.server.http:app",  # путь до приложения (используется при reload/workers)
        host="0.0.0.0",  # слушаем все интерфейсы (важно для Docker)
        port=8007,  # тот самый порт, на котором ждут payments-service
        workers=workers  # можно обрабатывать несколько запросов параллельно
    )


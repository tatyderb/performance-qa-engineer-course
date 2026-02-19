from pathlib import Path

from libs.logger import get_logger  # подключаем логгер
from libs.mock.loader import MockLoader  # импортируем класс загрузчика моков

# Инициализируем загрузчик моков
loader = MockLoader(
    root=Path("./services/payments/data"),  # путь к директории с мок-ответами (JSON)
    logger=get_logger("PAYMENTS_SERVICE_MOCK_LOADER")  # логгер с читаемым именем
)

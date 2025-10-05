from loguru import logger

logger.add(
    "info.log",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {module}:{function}:{line} - {message}",
    level="INFO",
    mode="w",
)
logger.info("Logger has started")

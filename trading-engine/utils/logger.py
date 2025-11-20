import logging

logger = logging.getLogger("trade_logger")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("logs/trading.log")
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

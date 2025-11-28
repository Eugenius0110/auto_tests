
import logging
import os
from datetime import datetime

def setup_logger():

    log_dir = "logs" # папка для логов, если ее нет
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

    logger = logging.getLogger('ui_tests')
    logger.setLevel(logging.INFO) # уровень __name__
    log_file = f"{log_dir}/test_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setLevel(logging.INFO)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    formatter = logging.Formatter(log_format)
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

logger = setup_logger()

import logging
import os


def get_logger():
    path = os.path.dirname(__file__)
    # Где 'task' - корневая директория проекта.
    abspath = path.split("task", 1)[0]
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('[%(asctime)s]: %(levelname)s: %(module)s: %(message)s', '%Y-%m-%d %H:%M:%S')
    file_handler = logging.FileHandler("%s/task/reports/report.log" % abspath, "w")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger

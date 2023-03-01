""" LOGGER """
import logging
from logging import Formatter


logger_api = logging.getLogger('api')
file_api = logging.FileHandler('logs/api.log')

logger_api.setLevel('INFO')
file_api.setFormatter(Formatter("%(asctime)s [%(levelname)s] %(message)s"))
logger_api.addHandler(file_api)

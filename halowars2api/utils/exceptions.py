# local imports
from .constants import HALO_DEV_URL


class ApiKeyException(Exception):
    def __init__(self, message='Please input a valid API key.\n'
                               f'If you do not have one, please visit: {HALO_DEV_URL}'):
        self._message = message
        super().__init__(self._message)

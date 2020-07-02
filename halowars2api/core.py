# third party imports
from requests import Session

# local app imports
from .utils.exceptions import ApiKeyException


class HaloWars2Api:
    def __init__(self, api_key: str = None):
        self._api_key = api_key
        self._session = Session()

        # if api key is passed to init method
        if api_key:
            self._format_api_key()
            self._update_session(self._api_key)

    def __call__(self, api_key: str = None):
        if (api_key is None) & (self._api_key is None):
            raise ApiKeyException()

        # if any api key is passed
        if api_key:
            self._api_key = api_key

        # if the api key is not a dictionary yet
        if not isinstance(self._api_key, dict):
            self._format_api_key()

        self._update_session(self._api_key)

    def __repr__(self):
        return f'Halo Wars 2 API: {self._api_key}'

    def __str__(self):
        return self.__repr__()

    def _format_api_key(self):
        self._api_key = {'Ocp-Apim-Subscription-Key': self._api_key}

    def _update_session(self, mapping: dict):
        self._session.headers.update(mapping)

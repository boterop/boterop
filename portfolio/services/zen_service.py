import requests


class ZenService(object):
    ZEN_URL = "https://zenquotes.io"
    API_URL = f"{ZEN_URL}/api"

    def get_quote(self):
        return requests.get(f"{self.API_URL}/random").json()

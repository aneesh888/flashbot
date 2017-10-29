import requests


class FlashGet(object):
    # Sends a GET request
    def __init__(url=None, headers=None, callback=None):
        self.url = url
        self.headers = headers
        self.callback = callback
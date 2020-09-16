from typing import Dict

import requests


class Api:
    def __init__(self):
        self.headers: Dict[str, str] = {
            "referer": "https://www.hltv.org/stats",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        }

    def get(self, url):
        return requests.get(url, headers=self.headers)

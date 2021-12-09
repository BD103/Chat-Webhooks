import json
import os
import typing as t

import requests

from chat_webhooks.errors import WebhookUrlNotFound


class ChatWebhook(object):
    webhook_url: t.Optional[str]
    headers: dict = {"Content-Type": "application/json; charset=UTF-8"}

    def __init__(self, webhook_url: str = None, headers: dict = None):
        self.webhook_url = webhook_url or os.getenv("WEBHOOK_URL")
        self.headers = headers or self.headers

        if self.webhook_url is None:
            raise WebhookUrlNotFound("Please give a webhook url.")

    def send(self, msg: str):
        return self._send(json.dumps({"text": msg}))

    def _send(self, data: t.Any):
        r = requests.post(self.webhook_url, data=data, headers=self.headers)
        return r

# Chat Webhooks

Easily interact and send messages with Google Chat's webhooks feature. This API is small, but should be a nice framework for working with any webhook.

## Installation

```shell
python -m pip install -U chat_webhooks
```

## Getting Started

```python
# API Example
from chat_webhooks import ChatWebhook

chat = ChatWebhook("WEBHOOK_URL")
chat.send("Hello, world!")
```

```shell
# Shell example
$ python -m chat_webhooks -w "WEBHOOK_URL"

# Interactive Google Chat webhook client
# Made by BD103

> Hello, world!
```

## More Documentation

You can view a short guide [here](https://bd103.github.io/Chat-Webhooks).

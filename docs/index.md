Chat-Webhooks is a small Python package that lets you easily interact with Google Chat's webhooks feature. Webhooks currently **only work for spaces**. If you have a direct message or legacy group chat, you won't be able to follow these steps.

You can also upgrade your legacy group chat to a space.

## Creating a Webhook

1. Select your Google Chat space and click **Manage webhooks**.
2. Enter in the name for your webhook, and optionally paste in the url for its image.
3. The screen should not display your created webhook. Click the copy symbol.
4. Save this webhook url for later use.

## Hello, world!

Take the url that you copied, and insert it into the following example.

```python
# hello.py
from chat_webhooks import ChatWebhook

url = "URL_YOU_COPIED"
chat = ChatWebhook(url)

chat.send("Hello, world!")
```

## Interactive Client

If you do not want to write a custom client, you can use the built in one.

```shell
# Set variable
export WEBHOOK_URL="URL"

python -m chat_webhooks
# Or
python -m chat_webhooks --webhook-url "URL"
```

## Custom JSON

Sometimes you want to send cards instead of plain text. You can create the JSON yourself.

```python
# card.py
from chat_webhooks import ChatWebhook
import json

url = "URL_YOU_COPIED"
chat = ChatWebhook(url)

msg = {
    "cards": [
        {
            "sections": [
                {
                    "widgets": [
                        {
                            "textParagraph": {
                                "text": '<b>Roses</b> are <font color="#ff0000">red</font>,<br><i>Violets</i> are <font color="#0000ff">blue</font>'
                            }
                        }
                    ]
                }
            ]
        }
    ]
}

chat._send(json.dumps(msg))
```

You can see more about card messages [here](https://developers.google.com/chat/api/guides/message-formats/cards).

## Further Reading

If you want more information on how webhooks work, you can [read the documentation here](https://developers.google.com/chat/quickstart/incoming-bot-python).

import sys

import click

from chat_webhooks import ChatWebhook
from chat_webhooks.errors import WebhookUrlNotFound


@click.command()
@click.option("-w", "--webhook-url", type=str, default=None)
@click.option("--color/--no-color", default=True)
def chat_webhooks(webhook_url: str, color: bool):
    if color:
        ansi_0 = "\x1b[0m"
        ansi_1 = "\x1b[34;1m"
        ansi_2 = "\x1b[94;1m"
    else:
        ansi_0 = ansi_1 = ansi_2 = ""

    try:
        chat = ChatWebhook(webhook_url)
    except WebhookUrlNotFound:
        print(
            f"""
You have not supplied a webhook url. You can pass it
by using the {ansi_2}--webhook-url{ansi_0} option. Make
sure to surround the url with double quotes.

    {ansi_2}python -m chat_webhooks --webhook-url "URL"{ansi_0}

You can also set it using an environmental variable.

    {ansi_2}export WEBHOOK_URL="URL"{ansi_0}

If you still need help, you can read the documentation.

    {ansi_2}https://bd103.github.io/Chat-Webhooks{ansi_0}
"""
        )
        sys.exit(1)

    print(f"{ansi_1}Interactive Google Chat webhook client{ansi_0}")
    print(f"Made by {ansi_2}BD103{ansi_0}\n")
    while True:
        try:
            msg = input("> ").strip()
        except EOFError:
            break

        chat.send(msg)
    print(f"\n{ansi_2}Exiting{ansi_0}")


if __name__ == "__main__":
    chat_webhooks()

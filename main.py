
from slack_bolt.adapter.socket_mode import SocketModeHandler
from utils.bot import SlackBot
import os


if __name__ == "__main__":
    bot = SlackBot()
    handler = SocketModeHandler(bot.app, os.environ["SLACK_APP_TOKEN"]) # Connecting to Slack via HTTP endpoint in case u want to listen for events
    bot.send_message(":wave: Bot is starting up!", channel="#general")
    handler.start()

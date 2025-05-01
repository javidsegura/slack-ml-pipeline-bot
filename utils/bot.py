
import os
from dotenv import load_dotenv
from slack_bolt import App

class SlackBot:
      def __init__(self):
        load_dotenv()
        self.app = App(
            token=os.environ["SLACK_BOT_TOKEN"],
            signing_secret=os.environ["SLACK_SIGNING_SECRET"]
        )
      
      def send_message(self, text: str, channel: str):  
            assert channel is not None, "Channel is required"
            try:
                  resp = self.app.client.chat_postMessage(channel=channel, text=text)
                  print("Message sent:", resp["ts"])
            except Exception as e:
                  print("Error sending message:", e)

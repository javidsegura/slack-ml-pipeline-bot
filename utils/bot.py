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

      def send_file(self, file_path: str, channel: str, title: str = None):
            """
            Sends a file (image, CSV, etc.) to the specified Slack channel.
            :param file_path: Path to the file to upload
            :param channel: Slack channel ID or name
            :param title: Optional title for the file
            """
            assert channel is not None, "Channel is required"
            assert os.path.isfile(file_path), f"File not found: {file_path}"
            try:
                  resp = self.app.client.files_upload(
                        channels=channel,
                        file=file_path,
                        title=title or os.path.basename(file_path)
                  )
                  print(f"File sent: {resp['file']['id']}")
            except Exception as e:
                  print(f"Error sending file: {e}")

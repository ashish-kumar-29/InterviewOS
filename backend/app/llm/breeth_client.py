import os
from dotenv import load_dotenv

load_dotenv()


class BreethClient:

    def __init__(self):

        self.api_key = os.getenv("BREETH_API_KEY")

    def generate(self, prompt: str):

        """
        Temporary stub.

        In the next step this will call
        Breeth MCP.

        """

        return prompt
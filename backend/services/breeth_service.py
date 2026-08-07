import os
import httpx

from dotenv import load_dotenv

load_dotenv()


class BreethService:

    def __init__(self):

        self.api_key = os.getenv("BREETH_API_KEY")

        self.base_url = "YOUR_BREETH_ENDPOINT"

    async def generate(self, prompt: str):

        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }

        payload = {
            "prompt": prompt
        }

        async with httpx.AsyncClient(timeout=60) as client:

            response = await client.post(
                self.base_url,
                json=payload,
                headers=headers
            )

        return response.json()
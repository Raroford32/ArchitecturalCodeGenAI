import requests
from config import OPENROUTER_API_BASE_URL, OPENAI_MODEL, OPENROUTER_API_KEY

class LLMClient:
    def __init__(self):
        self.base_url = OPENROUTER_API_BASE_URL
        self.model = OPENAI_MODEL
        self.api_key = OPENROUTER_API_KEY

    def generate_response(self, prompt):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}'
        }
        data = {
            'model': self.model,
            'messages': [
                {
                    'role': 'user',
                    'content': prompt
                }
            ],
            'max_tokens': 1024,
            'temperature': 0.7,
            'n': 1,
            'stop': None
        }
        response = requests.post(
            f"{self.base_url}/chat/completions",
            headers=headers,
            json=data
        )
        if response.status_code == 200:
            result = response.json()
            return result['choices'][0]['message']['content']
        else:
            raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

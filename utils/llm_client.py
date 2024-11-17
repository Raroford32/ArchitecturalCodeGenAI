import requests
import json
import logging
from config import OPENROUTER_API_BASE_URL, OPENAI_MODEL, OPENROUTER_API_KEY

class LLMClient:
    """Client for interacting with OpenRouter's LLM API"""
    
    def __init__(self):
        self.base_url = OPENROUTER_API_BASE_URL
        self.model = OPENAI_MODEL
        self.api_key = OPENROUTER_API_KEY
        
        # Configure logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def generate_response(self, prompt: str, max_tokens: int = 1024, temperature: float = 0.7) -> str:
        """
        Generate a response from the LLM using the provided prompt.
        
        Args:
            prompt (str): The input prompt for the model
            max_tokens (int): Maximum number of tokens to generate
            temperature (float): Sampling temperature (0.0 to 1.0)
            
        Returns:
            str: Generated response text
            
        Raises:
            Exception: If API request fails
        """
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}',
            'HTTP-Referer': 'https://your-app-domain.com',  # Required by OpenRouter
            'X-Title': 'AI Code Generator'  # Optional identifier
        }

        data = {
            'model': self.model,
            'messages': [
                {
                    'role': 'user',
                    'content': prompt
                }
            ],
            'max_tokens': max_tokens,
            'temperature': temperature,
            'n': 1,
            'stream': False
        }

        try:
            self.logger.info(f"Sending request to OpenRouter API with model: {self.model}")
            response = requests.post(
                f"{self.base_url}/chat/completions",
                headers=headers,
                json=data,
                timeout=30  # 30 second timeout
            )
            
            response.raise_for_status()
            result = response.json()
            
            if 'choices' in result and len(result['choices']) > 0:
                generated_text = result['choices'][0]['message']['content']
                self.logger.info("Successfully generated response")
                return generated_text
            else:
                raise Exception("No choices found in API response")
                
        except requests.exceptions.RequestException as e:
            self.logger.error(f"API request failed: {str(e)}")
            raise Exception(f"API request failed: {str(e)}")
        except json.JSONDecodeError as e:
            self.logger.error(f"Failed to parse API response: {str(e)}")
            raise Exception(f"Failed to parse API response: {str(e)}")
        except Exception as e:
            self.logger.error(f"Unexpected error: {str(e)}")
            raise

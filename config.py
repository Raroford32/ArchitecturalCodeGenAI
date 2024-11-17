import os

# Flask configuration
SECRET_KEY = os.environ.get('FLASK_SECRET_KEY', 'your-secret-key-here')
DEBUG = True

# OpenRouter API configuration
OPENROUTER_API_BASE_URL = 'https://openrouter.ai/api/v1'
OPENAI_MODEL = 'qwen/qwen-2.5-coder-32b-instruct'
OPENROUTER_API_KEY = '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'

# Redis configuration
REDIS_HOST = 'localhost'
REDIS_PORT = 6379  # Changed to standard Redis port
REDIS_DB = 0

# Output directories
OUTPUT_SRC_DIR = os.path.join(os.getcwd(), 'output', 'src')
OUTPUT_BUILD_DIR = os.path.join(os.getcwd(), 'output', 'build')

# Ensure output directories exist
os.makedirs(OUTPUT_SRC_DIR, exist_ok=True)
os.makedirs(OUTPUT_BUILD_DIR, exist_ok=True)

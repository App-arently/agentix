# config.py

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", None)
    COHERE_API_KEY = os.getenv("COHERE_API_KEY", None)
    SECRET_KEY = os.getenv("SECRET_KEY", 'default_secret_key')
    REDIS_URL = 'redis://localhost:6379/0'
    CELERY_BROKER_URL = REDIS_URL
    CELERY_RESULT_BACKEND = REDIS_URL

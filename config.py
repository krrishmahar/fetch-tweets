import os
from dotenv import load_dotenv


load_dotenv()

class Config:
    USER = os.environ.get('TWITTER_USERNAME') 
    EMAIL = os.environ.get('TWITTER_EMAIL') 
    PASSWORD = os.environ.get('TWITTER_PASSWORD') 
    TWEET_LIMIT = os.environ.get('TWEET_LIMIT') or 3
    TOKEN_GITHUB = os.environ.get('TOKEN_GITHUB') 

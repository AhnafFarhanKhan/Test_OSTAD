import os
from dotenv import load_dotenv

#Load environment variables from .env file
load_dotenv()
API_KEY = os.getenv("API_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")

print(f"Your API Key is: {API_KEY}")
print(f"Your Database URL is: {DATABASE_URL}")
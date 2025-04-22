import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DB_CONNECTION_STRING = os.getenv("DB_CONNECTION_STRING")  # e.g. postgresql+psycopg2://user:pass@localhost/dbname
EMBEDDING_MODEL = "text-embedding-3-small"
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# ENVIRONMENT VIRABLES
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SCRAPE_FISH_API_KEY = os.getenv("SCRAPE_FISH_API_KEY")

JINA_URI = os.getenv("JINA_URI")
SCRAPE_FISH_URI = os.getenv("SCRAPE_FISH_URI")
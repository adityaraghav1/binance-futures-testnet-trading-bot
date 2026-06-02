from binance.client import Client
from dotenv import load_dotenv
import os
load_dotenv()
API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_SECRET_KEY")
if not API_KEY or not API_SECRET:
    raise ValueError(
        "API keys not found in .env file"
    )
client = Client(
    API_KEY,
    API_SECRET,
    testnet=True
)

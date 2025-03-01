import os

API_ID = int(os.getenv("API_ID", "YOUR_API_ID"))
API_HASH = os.getenv("API_HASH", "YOUR_API_HASH")

MONGO_URI = os.getenv("MONGO_URI", "YOUR_MONGO_URI")

BOT_TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN")

LINK_CHANGE_INTERVAL = 6 * 60 * 60  # 6 hours in seconds

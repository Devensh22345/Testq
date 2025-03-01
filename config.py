import os

API_ID = int(os.getenv("API_ID", "22207976"))
API_HASH = os.getenv("API_HASH", "5c0ad7c48a86afac87630ba28b42560d")

MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://Test:Test@cluster0.pcpx5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

BOT_TOKEN = os.getenv("BOT_TOKEN", "7519708626:AAEY8r2HnXbUDPeySmj6qWkMqlJJmsnimGk")

LINK_CHANGE_INTERVAL = 6 * 60 * 60  # 6 hours in seconds

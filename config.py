import os

API_ID = int(os.getenv("API_ID", "29308061"))
API_HASH = os.getenv("API_HASH", "462de3dfc98fd938ef9c6ee31a72d099")

MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://Test:Test@cluster0.pcpx5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

BOT_TOKEN = os.getenv("BOT_TOKEN", "7519708626:AAEY8r2HnXbUDPeySmj6qWkMqlJJmsnimGk")

LINK_CHANGE_INTERVAL = 6 * 60 * 60  # 6 hours in seconds

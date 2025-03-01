from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio
from config import API_ID, API_HASH, BOT_TOKEN, LINK_CHANGE_INTERVAL
from plugins.change_link import change_channel_link
from plugins.login import ask_phone_number, process_phone_number, logout_command

# Initialize the bot client
app = Client("ChannelLinkChangerBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Start message
@app.on_message(filters.command("start") & filters.private)
async def start_command(client: Client, message: Message):
    await message.reply_text("hi")

# Change channel link instantly
@app.on_message(filters.command("change") & filters.private)
async def change_command(client: Client, message: Message):
    await message.reply_text("Changing the public channel link...")
    await change_channel_link(client)

# Automatically change channel links every 6 hours
async def auto_change_links():
    while True:
        await change_channel_link(app)
        await asyncio.sleep(LINK_CHANGE_INTERVAL)

# Login assistant account
@app.on_message(filters.command("login") & filters.private)
async def login_command(client: Client, message: Message):
    await ask_phone_number(client, message)

# Logout assistant account
@app.on_message(filters.command("logout") & filters.private)
async def handle_logout(client: Client, message: Message):
    await logout_command(client, message)

# Handle phone number input
@app.on_message(filters.text & filters.private)
async def handle_phone_number(client: Client, message: Message):
    await process_phone_number(client, message)

# Run the bot
if __name__ == "__main__":
    app.start()
    app.loop.create_task(auto_change_links())
    app.run()

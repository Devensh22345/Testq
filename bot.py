from pyrogram import Client, filters
from pyrogram.enums import ChatType
from pyrogram.types import Message
import asyncio
from config import API_ID, API_HASH, BOT_TOKEN, LINK_CHANGE_INTERVAL
from plugins.change_link import change_channel_link

app = Client("ChannelLinkChangerBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start") & filters.private)
async def start_command(client: Client, message: Message):
    await message.reply_text("hi")

@app.on_message(filters.command("change") & filters.private)
async def change_command(client: Client, message: Message):
    await message.reply_text("Changing the public channel link...")
    await change_channel_link(client)

async def auto_change_links():
    while True:
        await change_channel_link(app)
        await asyncio.sleep(LINK_CHANGE_INTERVAL)

@app.on_message(filters.command("login") & filters.private)
async def login_command(client: Client, message: Message):
    await message.reply_text("Send your phone number to log in the assistant account:")
    await app.send_message(message.chat.id, "Please enter your phone number.")

if __name__ == "__main__":
    app.start()
    app.loop.create_task(auto_change_links())
    app.run()
  

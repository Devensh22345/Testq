from pyrogram import Client, filters
from pyrogram.types import Message

async def ask_phone_number(client: Client, message: Message):
    await message.reply_text("Please send your phone number in international format (e.g., +1234567890).")

async def process_phone_number(client: Client, message: Message):
    phone_number = message.text
    await message.reply_text(f"Logging in with phone number: {phone_number}")
    try:
        await client.start(phone_number)
        await message.reply_text("Successfully logged in!")
    except Exception as e:
        await message.reply_text(f"Failed to log in: {e}")

async def logout_command(client: Client, message: Message):
    await message.reply_text("Logging out...")
    try:
        await client.stop()
        await message.reply_text("Successfully logged out!")
    except Exception as e:
        await message.reply_text(f"Failed to log out: {e}")

# Register handlers
Client.on_message(filters.command("login") & filters.private)(ask_phone_number)
Client.on_message(filters.text & filters.private)(process_phone_number)
Client.on_message(filters.command("logout") & filters.private)(logout_command)

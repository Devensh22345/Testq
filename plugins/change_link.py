import random
import string
from pyrogram import Client
from pyrogram.errors import FloodWait
import asyncio

async def change_channel_link(client: Client):
    async for dialog in client.get_dialogs():
        if dialog.chat.type == "channel" and dialog.chat.username:
            old_username = dialog.chat.username
            new_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=3))
            new_username = old_username[:-3] + new_suffix
            try:
                await client.update_username(dialog.chat.id, new_username)
                print(f"Changed channel link: {old_username} -> {new_username}")
            except FloodWait as e:
                print(f"FloodWait: Sleeping for {e.value} seconds.")
                await asyncio.sleep(e.value)
            except Exception as e:
                print(f"Failed to change link for {old_username}: {e}")
              

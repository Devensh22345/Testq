import asyncio
import random
from pyrogram import Client

async def change_channel_link(client: Client):
    async for dialog in client.get_dialogs():
        if dialog.chat.type == "channel":
            channel = dialog.chat
            try:
                # Generate a random link by changing the last 3 characters
                base_link = "examplechannel"
                random_suffix = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=3))
                new_link = f"{base_link}{random_suffix}"

                # Change the public channel link
                await client.set_chat_username(channel.id, new_link)
                print(f"Channel link changed to: {new_link}")

            except Exception as e:
                print(f"Failed to change link for {channel.title}: {e}")

async def auto_change_links(client: Client):
    while True:
        await change_channel_link(client)
        await asyncio.sleep(21600)  # 6 hours

import asyncio
from pyrogram import Client
from plugins.change_link import auto_change_links
from pyrogram.handlers import MessageHandler
from pyrogram import filters

app = Client("my_bot")

async def main():
    await app.start()
    print("Bot is running...")

    # Start the auto-change link task every 6 hours
    asyncio.create_task(auto_change_links(app))

    # Keep the bot running
    await asyncio.Event().wait()

# Handler for the '/change' command to manually change the link
async def change_link_handler(client, message):
    await message.reply("Changing the public channel link...")
    await auto_change_links(client)
    await message.reply("Public channel link changed successfully!")

# Add the '/change' command handler
app.add_handler(MessageHandler(change_link_handler, filters.command("change")))

# Run the bot
if __name__ == "__main__":
    asyncio.run(main())
    

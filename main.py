from rubpy import Client, filters
from rubpy.types import Update

bot = Client('hi')

@bot.on_message_updates(filters.is_me)
async def updates(update: Update):
    if update.text == "تست":
        print(update)
        await update.reply('hi')

bot.run()

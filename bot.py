import asyncio
import nest_asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Apply nest_asyncio to fix event loop issues
nest_asyncio.apply()

# Replace with your actual bot token
TOKEN = "7648688908:AAGQ8CaozzNnEutU7c-d4XDDdill8mNzlAY"

# Function to handle /start command
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Hello! Your bot is now active. 🚀")
    

async def model(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("select the model")

# Main function to run the bot
async def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("model", model))
    print("Bot is running...")
    await app.run_polling()

# Ensure it runs in VS Code & Jupyter without event loop issues
if __name__ == "__main__":
    asyncio.run(main())

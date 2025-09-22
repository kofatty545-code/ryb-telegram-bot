import os
from telegram.ext import Application, CommandHandler
from telegram import Update
from telegram.ext import ContextTypes

# Render မှာ Environment Variables ထဲကနေ ထည့်မယ်
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ RYB Bot is running successfully!")

# Bot setup
def main():
    if not TOKEN:
        raise SystemExit("❌ Missing TELEGRAM_BOT_TOKEN. Please set it in Render Environment Variables.")

    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    # Start long-polling
    app.run_polling()

if __name__ == "__main__":
    main()

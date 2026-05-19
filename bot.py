import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

users = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.username

    if user not in users:
        users[user] = 0

    await update.message.reply_text(
        f"Welcome @{user}\nYour Points: {users[user]}"
    )

async def points(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.username

    if user not in users:
        users[user] = 0

    await update.message.reply_text(
        f"@{user} Points = {users[user]}"
    )

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("points", points))

print("Bot Online ✅")

app.run_polling()

from telegram import Update
from telegram.ext import Application, MessageHandler, filters

TOKEN = "your api key here!"

async def get_file_id(update: Update, context):
    document = update.message.document
    if document:
        await update.message.reply_text(f"File ID: `{document.file_id}`")

app = Application.builder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.Document.ALL, get_file_id))

print("Bot is running... Send a PDF to get its File ID.")
app.run_polling()

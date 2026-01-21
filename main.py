import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Ciao! Sono VintedBabaBot\n\n"
        "Cerco scarpe da calcio sottoprezzo su Vinted.\n\n"
        "Comandi:\n"
        "/cerca - Cerca offerte\n"
        "/aiuto - Aiuto"
    )

async def aiuto(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Usa /cerca per iniziare ⚽")

async def cerca(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔍 Ricerca Vinted in arrivo...")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("aiuto", aiuto))
app.add_handler(CommandHandler("cerca", cerca))

app.run_polling()

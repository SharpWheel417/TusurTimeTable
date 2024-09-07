import time
from sympy import im
from telegram import Bot, Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters, CallbackQueryHandler, CallbackContext

# from config import ADMIN

from src.parsing.timetable import get_timetable

### Комманда Старт ###
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
  await context.bot.send_message(chat_id=update.effective_chat.id, text="Привет админ!",)


async def timetable(update: Update, context: ContextTypes.DEFAULT_TYPE):
  output = get_timetable()
  await context.bot.send_message(chat_id=update.effective_chat.id, text=output)

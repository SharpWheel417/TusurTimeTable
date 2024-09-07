from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackQueryHandler

from config import BOT_TOKEN


from src.controller.command import start, timetable


# sendmess("Бот запущен")

if __name__ == '__main__':
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # application.add_handler(CallbackQueryHandler(button_callback))

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    timetable_handler = CommandHandler('timetable', timetable)
    application.add_handler(timetable_handler)


    # message_handler = MessageHandler(filters.TEXT, handle_message)
    # application.add_handler(message_handler)


    application.run_polling()
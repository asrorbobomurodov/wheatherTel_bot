from telegram import Update
from telegram.ext import (CallbackContext, MessageHandler, 
                          Filters, CommandHandler, Updater)
from handlers import start, location, today_temp, weekly_wheather
from settings import TOKEN

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))

    # on non command i.e location - wheather the message on Telegram
    dp.add_handler(MessageHandler(Filters.location, location))
    dp.add_handler(MessageHandler(Filters.text('⛅️ Bugungi ob-havo'), today_temp))
    dp.add_handler(MessageHandler(Filters.text("📉 Haftalik ma'lumot"), weekly_wheather))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
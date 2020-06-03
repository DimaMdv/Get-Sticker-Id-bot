from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

#token input 
TOKEN = input("Enter the token:")
updater = Updater(token=TOKEN, use_context=True)

updater.start_polling()
updater.idle()
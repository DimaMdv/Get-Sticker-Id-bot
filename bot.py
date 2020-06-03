from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

#token input 
TOKEN = input("Enter the token:")
updater = Updater(token=TOKEN, use_context=True)

def start(update, context):#/start command function
    context.bot.send_message(chat_id=update.effective_chat.id, text = "Hello! Send me a sticker and I'll send you it's id.")


''' HANDLERS '''
updater.dispatcher.add_handler(CommandHandler('start', start))

updater.start_polling()
updater.idle()
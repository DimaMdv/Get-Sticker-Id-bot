from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
#logging config
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.WARNING)
logger = logging.getLogger(__name__)

#token input 
TOKEN = input("Enter the token:")
updater = Updater(token=TOKEN, use_context=True)


''' FUNCTIONS '''
def start(update, context):#/start command function
    context.bot.send_message(chat_id=update.effective_chat.id, text = "Hello! Send me a sticker and I'll send you it's id.")

def stickerId(update, context): #get sticker id
    context.bot.send_message(chat_id=update.effective_chat.id, text = "Here this sticker's id:")
    # "update.message.sticker.file_id" its a sticker id
    context.bot.send_message(chat_id=update.effective_chat.id, text = update.message.sticker.file_id)

def source(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text = "The source code of the bot:\ngithub.com/DimaTheCat/Get-Sticker-Id-bot")

def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


''' HANDLERS '''
updater.dispatcher.add_handler(CommandHandler('start', start))

updater.dispatcher.add_handler(MessageHandler(Filters.sticker, stickerId))

updater.dispatcher.add_handler(CommandHandler('source', source))

updater.dispatcher.add_handler(MessageHandler(Filters.regex('source'), source))

updater.dispatcher.add_error_handler(error)


updater.start_polling()
updater.idle()
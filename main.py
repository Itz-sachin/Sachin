from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

updater = Updater("5990943661:AAGTqDjLfw03VdeHiMD9eJOXWwFIGo8miVU", use_context=True)


def start(update: Update, context: CallbackContext):
	update.message.reply_text("Enter the text you want to show to the user whenever they start the bot")

updater.dispatcher.add_handler(CommandHandler('start', start))

 	
updater.start_polling()

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
logging.basicConfig (format = "%(name)s - %(levelname)s - %(message)s",
    level = logging.INFO,
    filename = "bot.log"
    )
def greet_user (bot, update):
    text = "Here /start"
    print (text)
    """print (1/0)"""
    update.message.reply_text(text)

def talk_to_me (bot, update):
    user_text = update.message.text
    logging.info (user_text)
    update.message.reply_text(user_text)
def main ():
    updater = Updater ("453979828:AAH8NOKrg5FnVjQnYbpb2ZAmZined84Agp0")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler (MessageHandler(Filters.text, talk_to_me))

    updater.start_polling()
    updater.idle()
   
main ()  
"""def get_answer(statement):

    dialogue = {"hi" : "hi, how are you", "how are you" : "fine, tnks", "bye" : "see you"}

    return  (dialogue [statement.lower()])

print (get_answer(input ("say smth ")))
while input() != "bye":
    get_answer(statement)"""

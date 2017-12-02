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
    user_text = update.message.text # то, что ввел пользователь
    logging.info (user_text) # сохранение в файл промежуточной информации
    update.message.reply_text(user_text) #ответ бота


def word_count(bot, update):
    phrase = update.message.text
    words_list = phrase.split(" ")
  
    update.message.reply_text( "Number of words is " + str(len(words_list) - 1))
    if len(words_list) - 1 == 0:
        update.message.reply_text("ну скажи что-нибудь")

def planet(bot, update):
    """update.message.reply_text("Enter the name of the planet in English, please")"""
    planet = update.message.text[8 :]
    import ephem
    import datetime

    date = datetime.datetime.now()
    date = date.strftime("%Y/%m/%d")
    astronomy = {"Mars" : ephem.Mars, "Venus" : ephem.Venus, "Jupiter" : ephem.Jupiter, "Mercury" : ephem.Mercury, "Saturn" : ephem.Saturn, 
 "Neptune" : ephem.Neptune, "Uranus" : ephem.Uranus}


   
    constellation = str(ephem.constellation(astronomy.get(planet, ephem.Neptune)(date)))
    update.message.reply_text(planet + " is in the " + constellation [7 : len(constellation)-1] + " constellation.")



def calc(bot, update):
    equation = update.message.text[6:]

    if equation[-1] != "=":
        update.message.reply_text("выражение должно иметь вид x + y = ")
    equation = equation[: -1]
    print (equation)

    if "+" in equation:
        equation_data = equation.split("+")
        print (equation_data)
        summ = int(equation_data[0]) + int(equation_data[1])
        update.message.reply_text("сумма  равняется " + str(summ))
    elif "-" in equation:
        equation_data = equation.split("-")
        subtraction = int(equation_data[0]) - int(equation_data[1])
        update.message.reply_text("разность  равняется " + str(subtraction))
    elif "/" in equation:
        equation_data = equation.split("/")
        division  = int(equation_data[0]) / int(equation_data[1])
        update.message.reply_text("результат деления равняется " + str(division))
    else:
        equation_data = equation.split("*")
        multiplication = int(equation_data[0]) * int(equation_data[1])
        update.message.reply_text("результат умножения равняется " + str(multiplication))

    





    # return print ("Number of words is " + str(len(words_list)))

def main ():
    updater = Updater ("453979828:AAH8NOKrg5FnVjQnYbpb2ZAmZined84Agp0")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("wordcount", word_count))
    dp.add_handler(CommandHandler("calc", calc))
    dp.add_handler (MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler("planet", planet))

    updater.start_polling()
    updater.idle()

   
main ()  
"""def get_answer(statement):

    dialogue = {"hi" : "hi, how are you", "how are you" : "fine, tnks", "bye" : "see you"}

    return  (dialogue [statement.lower()])

print (get_answer(input ("say smth ")))
while input() != "bye":
    get_answer(statement)"""

import telebot
from telebot import types
from decouple import config


bot = telebot.TeleBot(config('TOKEN'))

def hello_example():
    # Using the ReplyKeyboardMarkup class
    # It's constructor can take the following optional arguments:
    # - resize_keyboard: True/False (default False)
    # - one_time_keyboard: True/False (default False)
    # - selective: True/False (default False)
    # - row_width: integer (default 3)
    # row_width is used in combination with the add() function.
    # It defines how many buttons are fit on each row before continuing on the next row.
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('a')
    itembtn2 = types.KeyboardButton('b')
    itembtn3 = types.KeyboardButton('c')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.send_message(config("CHATID", cast=int), 'Choose one letter:', reply_markup=markup)

def second_example():
    # or add KeyboardButton one row at a time:
    markup = types.ReplyKeyboardMarkup()
    itembtna = types.KeyboardButton('a')
    itembtnv = types.KeyboardButton('v')
    itembtnc = types.KeyboardButton('c')
    itembtnd = types.KeyboardButton('d')
    itembtne = types.KeyboardButton('e')
    markup.row(itembtna, itembtnv)
    markup.row(itembtnc, itembtnd, itembtne)
    bot.send_message(config("CHATID", cast=int), "Choose one letter:", reply_markup=markup)

def removeReplykeyboard():
    # ReplyKeyboardRemove: hides a previously sent ReplyKeyboardMarkup
    # Takes an optional selective argument (True/False, default False)
    markup = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(config("CHATID", cast=int), 'removendo', reply_markup=markup)

if __name__ == '__main__':
    # uncomment that you want to use

    #hello_example()
    #second_example()
    #removeReplykeyboard()
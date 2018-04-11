import telebot
from decouple import config

bot = telebot.TeleBot(config('TOKEN'))

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    print(message)
    bot.reply_to(message, "Howdy, How are you doing?")

@bot.message_handler(commands=['binance'])
def send_binance(message):
    print(message)
    bot.reply_to(message, "Compre x por y e etc.")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    print(message)
    bot.reply_to(message, message.text)

def main():
    bot.polling()

if __name__ == '__main__':
    main()

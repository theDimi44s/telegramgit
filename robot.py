#coding:utf-8
import telebot, config
bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Приветствую! Я ж/д бот!")
if __name__ == "__main__":
    bot.polling()
@bot.message_handler(commands=["help"])
def start(message):
    bot.send_message(message.chat.id, "/start - початок використання\n/help - допомога")
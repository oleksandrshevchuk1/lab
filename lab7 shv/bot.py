import os
from dotenv import load_dotenv
from telebot import TeleBot

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(
        message,
        "Привіт! Я Ехо-Бот.\n"
        "Надішли мені будь-яке повідомлення, і я повторю його назад.\n"
        "Я готовий до роботи!"
    )

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

def main():
    print("Бот запущений і чекає повідомлення...")
    bot.infinity_polling()

if __name__ == "__main__":
    main()

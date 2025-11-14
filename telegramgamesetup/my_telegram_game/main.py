import os
from dotenv import load_dotenv
from telebot import TeleBot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from game import story, game_engine
from utils.keyboards import generate_choices_keyboard

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
bot = TeleBot(TOKEN)

# --- Привітання при /start ---
@bot.message_handler(commands=["start"])
def start_message(message):
    chat_id = message.chat.id
    welcome_text = "Привіт!😃 Ласкаво просимо у гру.\nНатисни кнопку, щоб почати пригоди."
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(text="Почати гру🌌", callback_data="start_game"))
    bot.send_message(chat_id, welcome_text, reply_markup=keyboard)

# --- Відправка вузла гри ---
def send_node(chat_id, node_id):
    node = story.get_node(node_id)
    if not node:
        bot.send_message(chat_id, "Сюжет не знайдено.")
        return

    text = node["text"]
    choices = node.get("choices", {})

    # Відправляємо текст
    bot.send_message(chat_id, text)

    # Якщо є вибори, додаємо кнопки
    if choices:
        keyboard = generate_choices_keyboard(choices)
        bot.send_message(chat_id, "🧠Виберіть варіант🏃‍♂️:", reply_markup=keyboard)

# --- Обробка натискання кнопок ---
@bot.callback_query_handler(func=lambda call: True)
def handle_choice(call):
    chat_id = call.message.chat.id
    data = call.data

    if data == "start_game":
        # Почати гру з вузла "start"
        game_engine.set_user_progress(chat_id, "start")
        send_node(chat_id, "start")
    else:
        # Інші вибори гри
        game_engine.set_user_progress(chat_id, data)
        send_node(chat_id, data)

# --- Запуск бота ---
bot.infinity_polling()

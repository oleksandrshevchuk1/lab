from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def generate_choices_keyboard(choices: dict):
    keyboard = InlineKeyboardMarkup()
    for text, callback in choices.items():
        keyboard.add(InlineKeyboardButton(text=text, callback_data=callback))
    return keyboard
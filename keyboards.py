from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


def create_board(answers):
    button_hi1 = KeyboardButton(answers[0])
    button_hi2 = KeyboardButton(answers[1])
    button_hi3 = KeyboardButton(answers[2])
    button_hi4 = KeyboardButton(answers[3])

    greet_kb = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    greet_kb.add(button_hi1, button_hi2, button_hi3, button_hi4)
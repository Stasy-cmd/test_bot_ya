import emoji
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_text_hello():
    text_hello = (
        "Привет! Меня зовут Настя :red_heart: \n"
        "Рада, что ты используешь этого бота, чтобы <i> познакомиться со мной поближе! </i> \n\n\n"
    )
    return text_hello


def get_menu():
    menu = (
        "Напиши <b>/nextstep: фото</b> , чтобы увидеть мое последнее селфи \n"
        "Напиши <b>/nextstep: селфи</b> , чтобы увидеть мое фото из старшей школы \n"
        "Напиши <b>/nextstep: пост</b> прочитать небольшой пост о моем главном увлечении \n"
        "Напиши <b>/nextstep: GPT</b> и узнаешь, что такое GPT \n"
        "Напиши <b>/nextstep: бд</b> и поймешь разницу между SQL и NoSQL \n"
        "Напиши <b>/nextstep: любовь</b> послушаешь мою историю первой любви \n"
        "Напиши <b>/nextstep: ссылка</b> и получишь ссылку на репозиторий данного бота \n"
        "Напиши <b>/menu</b> и бот выведет меню"
    )
    return menu


def get_next_step():
    text_next = "Введите параметр для команды \nили воспользуйтесь подсказкой из меню - /menu \n"
    return text_next


def get_post():
    post = (
        "Кроме музыки, \n"
        "особое место в моем :red_heart: занимают рисунки. \n\n"
        "Я просто обожаю рисовать на планшете для себя в свободное время. \n"
        "Вот некоторые из моих работ. :up_arrow:\n"
    )
    return post


def get_button_all():
    btn1 = types.KeyboardButton(emoji.emojize(":eyes: Увидеть"))
    btn2 = types.KeyboardButton(emoji.emojize(":ear: Послушать"))
    btn3 = types.KeyboardButton(emoji.emojize(":laptop: Ссылка на репозиторий"))
    btn4 = types.KeyboardButton(emoji.emojize(":open_hands: Помощь"))

    markup = types.reply_keyboard.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(btn1, btn2)
    markup.row(btn3, btn4)

    return markup


def get_button_url():
    url = InlineKeyboardMarkup(row_width=1)
    urlButton = InlineKeyboardButton(
        text="Перейти в репозиторий", url="https://github.com/Stasy-cmd/test_bot_ya"
    )
    url.add(urlButton)
    return url


def get_button_views():
    btn1 = types.KeyboardButton(emoji.emojize(":selfie: Последнее селфи"))
    btn2 = types.KeyboardButton(emoji.emojize(":school: Фото из старшей школы"))
    btn3 = types.KeyboardButton(
        emoji.emojize(":sparkles: Небольшой пост о моем главном увлечении")
    )
    btn4 = types.KeyboardButton(emoji.emojize(":left_arrow: Назад"))
    btn5 = types.KeyboardButton(emoji.emojize(":open_hands: Помощь"))

    markup = types.reply_keyboard.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(btn1, btn2, btn3)
    markup.row(btn4, btn5)

    return markup


def get_button_listen():
    btn1 = types.KeyboardButton(emoji.emojize(":light_bulb: Что такое GPT"))
    btn2 = types.KeyboardButton(
        emoji.emojize(":face_screaming_in_fear:  Разница между SQL и NoSQL")
    )
    btn3 = types.KeyboardButton(
        emoji.emojize(":magnifying_glass_tilted_right: История моей первой любви")
    )
    btn4 = types.KeyboardButton(emoji.emojize(":left_arrow: Назад"))
    btn5 = types.KeyboardButton(emoji.emojize(":open_hands: Помощь"))

    markup = types.reply_keyboard.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(btn1, btn2, btn3)
    markup.row(btn4, btn5)

    return markup

from aiogram import types
import emoji

from bot.utils import (
    get_menu,
    get_text_hello,
    get_button_all,
    get_button_views,
    get_post,
    get_button_url,
    get_next_step,
    get_button_listen,
)


async def start_command(message: types.Message):
    start_text = get_text_hello() + get_menu()
    await message.answer(
        emoji.emojize(start_text), parse_mode="HTML", reply_markup=get_button_all()
    )


async def menu_command(message: types.Message):
    start_text = get_menu()
    await message.answer(
        emoji.emojize(start_text), parse_mode="HTML", reply_markup=get_button_all()
    )


async def button_menu_command(message: types.Message):
    await message.answer(
        "<b>Главное меню</b>", parse_mode="HTML", reply_markup=get_button_all()
    )


async def listen_menu_command(message: types.Message):
    await message.answer(
        "<b>На какую тему поговорим?</b>",
        parse_mode="HTML",
        reply_markup=get_button_listen(),
    )


async def see_menu_command(message: types.Message):
    await message.answer(
        "<b>Что хотите прочитать?</b>",
        parse_mode="HTML",
        reply_markup=get_button_views(),
    )


async def next_command(message: types.Message):
    next_text = get_next_step()
    await message.answer(
        emoji.emojize(next_text), parse_mode="HTML", reply_markup=get_button_all()
    )


async def photo_command(message: types.Message):
    photo = open("../data/school.jpg", "rb")
    caption = emoji.emojize(
        "А это я в 11-м классе со своей\n"
        "любимой учительницей:smiling_face_with_sunglasses:"
    )
    await message.answer_photo(photo, caption=caption, reply_markup=get_button_views())


async def gpt_command(message: types.Message):
    with open("../data/gpt.m4a", mode="rb") as file:
        binary_content = file.read()
    await message.answer_voice(binary_content, reply_markup=get_button_listen())


async def bd_command(message: types.Message):
    with open("../data/db.m4a", mode="rb") as file:
        binary_content = file.read()
    await message.answer_voice(binary_content, reply_markup=get_button_listen())


async def love_command(message: types.Message):
    with open("../data/love.m4a", mode="rb") as file:
        binary_content = file.read()
    await message.answer_voice(binary_content, reply_markup=get_button_listen())


async def self_command(message: types.Message):
    photo = open("../data/self.png", "rb")
    caption = emoji.emojize("Привет-привет :victory_hand:")
    await message.answer_photo(photo, caption=caption, reply_markup=get_button_views())


async def url_command(message: types.Message):
    text = emoji.emojize("Мой репозиторий :victory_hand:")
    await message.answer(text,reply_markup=get_button_url())
    

async def post_command(message: types.Message):
    text = emoji.emojize(get_post())
    media = types.MediaGroup()
    media.attach_photo(types.InputFile("../data/post/1.png"), text)
    media.attach_photo(types.InputFile("../data/post/2.jpg"))
    media.attach_photo(types.InputFile("../data/post/3.png"))
    media.attach_photo(types.InputFile("../data/post/4.jpg"))
    media.attach_video(types.InputFile("../data/post/video.MOV"))
    await message.answer_media_group(media=media)
    await message.answer(
        "<b>Главное меню</b>", parse_mode="HTML", reply_markup=get_button_all()
    )

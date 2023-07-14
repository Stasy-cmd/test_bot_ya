from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from bot.commands import (
    start_command,
    photo_command,
    gpt_command,
    self_command,
    next_command,
    menu_command,
    bd_command,
    love_command,
    post_command,
    url_command,
    button_menu_command,
    see_menu_command,
    listen_menu_command,
)

from config import settings

bot = Bot(token=settings.bot_token)
storage = MemoryStorage()

if __name__ == "__main__":
    dp = Dispatcher(bot, storage=storage)

    dp.register_message_handler(start_command, commands=["start"])
    dp.register_message_handler(next_command, commands=["nextstep"])
    dp.register_message_handler(menu_command, commands=["menu"])

    dp.register_message_handler(
        photo_command, lambda message: "фото" in message.text.lower()
    )
    dp.register_message_handler(
        self_command, lambda message: "селфи" in message.text.lower()
    )
    dp.register_message_handler(
        gpt_command, lambda message: "gpt" in message.text.lower()
    )
    dp.register_message_handler(
        bd_command, lambda message: "бд" in message.text.lower()
    )
    dp.register_message_handler(
        love_command, lambda message: "любовь" in message.text.lower()
    )
    dp.register_message_handler(
        post_command, lambda message: "пост" in message.text.lower()
    )
    dp.register_message_handler(
        url_command, lambda message: "ссылка" in message.text.lower()
    )

    dp.register_message_handler(
        button_menu_command, lambda message: "назад" in message.text.lower()
    )
    dp.register_message_handler(
        see_menu_command, lambda message: "увидеть" in message.text.lower()
    )
    dp.register_message_handler(
        listen_menu_command, lambda message: "послушать" in message.text.lower()
    )
    dp.register_message_handler(
        bd_command, lambda message: "разница между sql и nosql" in message.text.lower()
    )
    dp.register_message_handler(
        love_command,
        lambda message: "история моей первой любви" in message.text.lower(),
    )
    dp.register_message_handler(
        menu_command, lambda message: "помощь" in message.text.lower()
    )

    dp.message_handler(start_command, commands=["see_menu"])

    executor.start_polling(dp, skip_updates=True)

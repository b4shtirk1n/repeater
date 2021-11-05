import asyncio
import aiogram

from aiogram import Bot, Dispatcher, executor
from aiogram.types.message import Message
from config import BOT_TOKEN, admin_id

loop = asyncio.get_event_loop()
bot = Bot(BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, loop=loop)

@dp.message_handler(content_types=["photo"])
async def get_photo(message: Message):
    file_id = message.photo[-1].file_id
    await bot.send_photo(message.chat.id, file_id)
    await bot.send_photo(admin_id, file_id)
    await bot.send_message(chat_id=admin_id, text = f"от: @{message.from_user.username}")
    print()
    print(message.from_user.id, message.from_user.first_name, message.from_user.last_name)
    print(message.from_user.username, file_id)

@dp.message_handler(content_types=["sticker"])
async def get_photo(message: Message):
    file_id = message.sticker.file_id
    await bot.send_sticker(message.chat.id, file_id)
    await bot.send_message(chat_id=admin_id, text = f"от: @{message.from_user.username}")
    print()
    print(message.from_user.id, message.from_user.first_name, message.from_user.last_name)
    print(message.from_user.username, file_id)

if __name__ == "__main__":
    from handlers import dp, send_to_admin
    executor.start_polling(dp, skip_updates=True, on_startup=send_to_admin)


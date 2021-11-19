from aiogram.types import Message, ContentType, ReplyKeyboardRemove
from aiogram.dispatcher.filters import Text
from data import dp, db
from Keyboards.default import level


@dp.message_handler(commands=["start"])
async def start_handler(message: Message):
    user_id = message.from_user.id
    existing_user = await db.select_user(user_id)
    if not existing_user:
        username = message.from_user.username
        first_name = message.from_user.first_name
        last_name = message.from_user.last_name
        await db.add_user(user_id, username, first_name, last_name)
    await message.answer("Выберите свой уровень", reply_markup=level)


@dp.message_handler(
    Text(equals=[
        "Beginner",
        "Elementary",
        "Pre-Intermediate",
        "Intermediate",
        "Upper-Intermediate",
        "Advanced",
        "IELTS"
    ]))
async def add_level(message: Message):
    user_level = str(message.text)
    await db.update_user(message.from_user.id, user_level)
    await message.answer(f"Ваш уровень <b>{message.text}</b>", reply_markup=ReplyKeyboardRemove())


@dp.message_handler(content_types=ContentType.VOICE)
async def get_file_id_v(message: Message):
    # await message.reply(message.voice.file_id)
    await message.answer_voice("AwACAgIAAxkBAAM_YZZaFICk8Kdkrg-wd5JvUpppR4MAAlURAAJB9bhI7jsQuyduIqciBA",
                               caption="voice"
                               )

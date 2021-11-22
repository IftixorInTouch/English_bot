from aiogram.types import Message, ContentType, ReplyKeyboardRemove
from aiogram.dispatcher.filters import Text
from data import dp, db
from Keyboards.default import level, beginner, elementary
from States.states import States
from aiogram.dispatcher import FSMContext


@dp.message_handler(commands=["start"])
async def start_handler(message: Message):
    user_id = message.from_user.id
    existing_user = await db.select_user(user_id)
    if not existing_user:
        username = message.from_user.username
        first_name = message.from_user.first_name
        last_name = message.from_user.last_name
        await db.add_user(user_id, username, first_name, last_name)
    await message.answer("<b>Выберите свой уровень</b>", reply_markup=level)


@dp.message_handler(
    Text(equals=[
        "Beginner",
        "Elementary",
        "Pre-Intermediate",
        "Intermediate",
        "Upper-Intermediate",
        "Advanced",
        "IELTS",
    ]))
async def add_level(message: Message):
    user_level = str(message.text)
    await db.update_user(message.from_user.id, user_level)
    if message.text == "Beginner":
        await message.answer(f"<b>Выберите юнит</b>", reply_markup=beginner)
        await States.Choose_unit.set()
    elif message.text == "Elementary":
        await message.answer(f"<b>Выберите юнит</b>", reply_markup=elementary)
        await States.Choose_unit.set()
    elif message.text == "Pre-Intermediate":
        pass
    elif message.text == "Intermediate":
        pass
    elif message.text == "Upper-Intermediate":
        pass
    elif message.text == "Advanced":
        pass
    elif message.text == "IELTS":
        pass


@dp.message_handler(state=States.Choose_unit)
async def choose_unit(message: Message, state: FSMContext):
    if message.text == "Назад":
        await message.answer("Назад", reply_markup=level)
        await state.finish()
        return
    unit = int(message.text)
    audios = await db.select_file_ids_by_unit(unit)

    for word in audios:
        await dp.bot.send_audio(chat_id=message.chat.id, audio=word[0])


@dp.message_handler(content_types=ContentType.AUDIO)
async def get_file_id_v(message: Message):
    file_id = await message.reply(message.audio.file_id)
    file_name = message.audio.file_name
    for i in range(0, len(file_name)):
        if file_name[i] == '-':
            file_name = file_name[:i - 1]
            print(file_name)
            break
    await db.update_add_file_id(file_id.text, file_name)

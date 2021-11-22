from data import dp
from aiogram.types import Message
from States.states import States
from aiogram.dispatcher import FSMContext
from Keyboards.default import lang
from googletrans import Translator


@dp.message_handler(commands=["translator"])
async def translator(message: Message):
    await message.answer("Выберите язык", reply_markup=lang)


@dp.message_handler(text="Русский-Английский")
async def rus_eng(message: Message):
    await States.Translate.set()
    await message.answer("<b>Введите предложение</b>")


@dp.message_handler(state=States.Translate)
async def translating(message: Message, state: FSMContext):
    print(message.text)
    ru_en = Translator()
    t = ru_en.translate(message.text, 'en')

    print("hello")
    await message.answer()
    await state.finish()


@dp.message_handler(text="Английский-Русский")
async def eng_rus(message: Message):
    translation = Translator.translate(message.text, "ru")
    await message.answer(translation)

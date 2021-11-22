from aiogram.dispatcher.filters.state import StatesGroup, State


class States(StatesGroup):
    Choose_unit = State()
    Translate = State()

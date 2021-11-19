from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

level = ReplyKeyboardMarkup(resize_keyboard=True,
                            one_time_keyboard=True,
                            keyboard=[
                                [
                                    KeyboardButton("Beginner"),
                                    KeyboardButton("Elementary")
                                ],
                                [
                                    KeyboardButton("Pre-Intermediate"),
                                    KeyboardButton("Intermediate")
                                ],
                                [
                                    KeyboardButton("Upper-Intermediate"),
                                    KeyboardButton("Advanced")
                                ],
                                [
                                    KeyboardButton("IELTS")
                                ]
                            ])

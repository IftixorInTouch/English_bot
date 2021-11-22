from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

lang = ReplyKeyboardMarkup(resize_keyboard=True,
                           keyboard=[
                               [
                                   KeyboardButton("Русский-Английский")
                               ],
                               [
                                   KeyboardButton("Английский-Русский")
                               ]
                           ])

level = ReplyKeyboardMarkup(resize_keyboard=True,
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

beginner = ReplyKeyboardMarkup(resize_keyboard=True,
                               keyboard=[
                                   [
                                       KeyboardButton("1"),
                                       KeyboardButton("2"),
                                       KeyboardButton("3"),
                                       KeyboardButton("4")
                                   ],
                                   [
                                       KeyboardButton("5"),
                                       KeyboardButton("6"),
                                       KeyboardButton("7"),
                                       KeyboardButton("8")
                                   ],
                                   [
                                       KeyboardButton("9"),
                                       KeyboardButton("10"),
                                       KeyboardButton("11"),
                                       KeyboardButton("12")
                                   ],
                                   [
                                       KeyboardButton("13"),
                                       KeyboardButton("14"),
                                   ],
                                   [
                                       KeyboardButton("Назад")
                                   ]
                               ])
elementary = ReplyKeyboardMarkup(resize_keyboard=True,
                                 keyboard=[
                                     [
                                         KeyboardButton("1"),
                                         KeyboardButton("2"),
                                         KeyboardButton("3"),
                                     ],
                                     [
                                         KeyboardButton("4"),
                                         KeyboardButton("5"),
                                         KeyboardButton("6"),
                                     ],
                                     [
                                         KeyboardButton("7"),
                                         KeyboardButton("8"),
                                         KeyboardButton("9"),
                                     ],
                                     [
                                         KeyboardButton("10"),
                                         KeyboardButton("11"),
                                         KeyboardButton("12"),
                                     ],
                                     [
                                         KeyboardButton("Назад")
                                     ]
                                 ])

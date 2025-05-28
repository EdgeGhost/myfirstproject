from telebot import types
from telebot.types import InlineKeyboardMarkup

#Кнопки фракций агентов
fractions = InlineKeyboardMarkup(row_width=1)
fraction_btn_hares = types.InlineKeyboardButton('Хитрые зайцы 🐰', callback_data='curning_hares')
fraction_btn_victoria = types.InlineKeyboardButton('Домашний сервис Виктория ✨', callback_data='victoria')
fraction_btn_belobog = types.InlineKeyboardButton('Строительная компания Белобог 🛠', callback_data='belobog')
fractions.add(fraction_btn_hares,fraction_btn_victoria,fraction_btn_belobog)

#Фракция Хитрые Зайцы
curning_hares = InlineKeyboardMarkup(row_width=1)
curning_hares_agent1 = types.InlineKeyboardButton('Николь Демара 💵', callback_data='Николь Демара')
curning_hares_agent2 = types.InlineKeyboardButton('Энби Демара 🍔', callback_data='Энби Демара')
curning_hares_agent3 = types.InlineKeyboardButton('Билли Кид 🔫', callback_data='Билли Кид')
curning_hares_agent4 = types.InlineKeyboardButton('Нэкомия Мана 🐱', callback_data='Нэкомия Мана')
back_btn_curning = types.InlineKeyboardButton("🔙 Назад", callback_data="back_curning")
curning_hares.add(curning_hares_agent1,curning_hares_agent2,curning_hares_agent3,curning_hares_agent4,back_btn_curning)

#Фракция Виктория Хаускипинг
housekeeping_victoria = InlineKeyboardMarkup(row_width=1)
housekeeping_victoria_agent1 = types.InlineKeyboardButton('Von Lycaon 🐺', callback_data='Люкаон')
housekeeping_victoria_agent2 = types.InlineKeyboardButton('Александрина 🩶', callback_data='Александрина')
housekeeping_victoria_agent3 = types.InlineKeyboardButton('Corin Wickes 🪚', callback_data='Корин Уикс')
housekeeping_victoria_agent4 = types.InlineKeyboardButton('Ellen Joe 🦈', callback_data='Эллен Джое')
back_btn_victoria = types.InlineKeyboardButton("🔙 Назад", callback_data="back_victoria")
housekeeping_victoria.add(housekeeping_victoria_agent1,housekeeping_victoria_agent2,
                          housekeeping_victoria_agent3, housekeeping_victoria_agent4,back_btn_victoria)

#Фракция Строительная компания Белобог
belobog = InlineKeyboardMarkup(row_width=1)
belobog_agent1 = types.InlineKeyboardButton('Koleda Belobog 🔨', callback_data='Коляда Белобог')
belobog_agent2 = types.InlineKeyboardButton('Grace Howard 👩🏻‍💻', callback_data='Грейс Ховард')
belobog_agent3 = types.InlineKeyboardButton('Ben Bigger 🐻', callback_data='Бен Биггер')
belobog_agent4 = types.InlineKeyboardButton('Anton Ivanov 🦾', callback_data='Антон Иванов')
back_btn_belobog = types.InlineKeyboardButton("🔙 Назад", callback_data="back_belobog")
belobog.add(belobog_agent1,belobog_agent2,belobog_agent3,belobog_agent4,back_btn_belobog)

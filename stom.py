from telebot import types

def oneStom(bot, message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    item1 = types.KeyboardButton("Науки о жизни")
    item2 = types.KeyboardButton("Техники мышления")
    item3 = types.KeyboardButton("Персональная эффективность")
    item4 = types.KeyboardButton("Основы НИР и проектной деятельности")
    item5 = types.KeyboardButton("Анатомия человека")
    item6 = types.KeyboardButton("Правовая грамотность")
    item7 = types.KeyboardButton("Химия")
    item8 = types.KeyboardButton("Иностранный язык")
    item9 = types.KeyboardButton("Латинский язык")
    item10 = types.KeyboardButton("История России")
    item11 = types.KeyboardButton("Управление личной безопасностью")
    item12 = types.KeyboardButton("Физика, математика")
    item13 = types.KeyboardButton("Философия")
    item12 = types.KeyboardButton("Эффективные коммуникации")
    item13 = types.KeyboardButton("Практикум по первой помощи")
    item14 = types.KeyboardButton("Физическая культура и спорт")
    back = types.KeyboardButton("🔙 Назад 🦷")

    markup.add(item1, item2, item3, item4, 
               item5, item6, item7, item8, item9, item10, item11, item12, item13, item14, back)

    bot.send_message(message.chat.id, '💮 Предмет (листать вниз)'.format(message.from_user), reply_markup=markup)


def twoStom(bot, message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    item1 = types.KeyboardButton("Основы материаловедения")
    item2 = types.KeyboardButton("Сестринское дело")
    item3 = types.KeyboardButton("Экономическая грамотность")
    item4 = types.KeyboardButton("Биостатистика")
    item5 = types.KeyboardButton("Микробиология")
    item6 = types.KeyboardButton("Патофизиология")
    item7 = types.KeyboardButton("Топографическая анатомия головы и шеи")
    item8 = types.KeyboardButton("Биохимия")
    item9 = types.KeyboardButton("Нормальная физиология")
    item10 = types.KeyboardButton("Пропедевтика стоматологических заболеваний")
    item15 = types.KeyboardButton("Физическая культура и спорт")
    back = types.KeyboardButton("🔙 Назад 🦷")

    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item15, back)

    bot.send_message(message.chat.id, '💮 Предмет (листать вниз)'.format(message.from_user), reply_markup=markup)


def threeStom(bot, message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    item1 = types.KeyboardButton("Фармакология")
    item2 = types.KeyboardButton("Патологическая анатомия")
    item3 = types.KeyboardButton("Внутренние болезни")
    item4 = types.KeyboardButton("Хирургические болезни")
    item5 = types.KeyboardButton("Лучевая диагностика")
    item6 = types.KeyboardButton("Гигиена, эпидемиология")
    item7 = types.KeyboardButton("Профилактика стоматологических заболеваний")
    item8 = types.KeyboardButton("Общественное здоровье и здравоохранение")
    item9 = types.KeyboardButton("Дерматовенерология")
    item10 = types.KeyboardButton("Неврология")
    item12 = types.KeyboardButton("Физическая культура и спорт")

    back = types.KeyboardButton("🔙 Назад 🦷")

    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item12, back)

    bot.send_message(message.chat.id, '💮 Предмет (листать вниз)'.format(message.from_user), reply_markup=markup)


def fourStom(bot, message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    item1 = types.KeyboardButton("Детская стоматология")
    item2 = types.KeyboardButton("Акушерство")
    item3 = types.KeyboardButton("Психиатрия, медицинская психология")
    item4 = types.KeyboardButton("Педиатрия")
    item5 = types.KeyboardButton("Оториноларингология")
    item6 = types.KeyboardButton("Офтальмология")
    item7 = types.KeyboardButton("Правовое обеспечение профессиональной деятельности")
    item8 = types.KeyboardButton("Судебная медицина")
    item9 = types.KeyboardButton("Инфекционные болезни, фтизиатрия")
    item13 = types.KeyboardButton("Физическая культура и спорт")
    back = types.KeyboardButton("🔙 Назад 🦷")

    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item13, back)

    bot.send_message(message.chat.id, '💮 Предмет (листать вниз)'.format(message.from_user), reply_markup=markup)


def fiveStom(bot, message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    item1 = types.KeyboardButton("Хирургическая стоматология")
    item2 = types.KeyboardButton("Ортодонтия и детское протезирование")
    item3 = types.KeyboardButton("Ортопедическая стоматология")
    item4 = types.KeyboardButton("Челюстно-лицевая хирургия")
    item5 = types.KeyboardButton("Медицина чрезвычайных ситуаций")
    item6 = types.KeyboardButton("Терапевтическая стоматология")
    item10 = types.KeyboardButton("Физическая культура и спорт")
    back = types.KeyboardButton("🔙 Назад 🦷")

    markup.add(item1, item2, item3, item4, item5, item6, item10, back)

    bot.send_message(message.chat.id, '💮 Предмет (листать вниз)'.format(message.from_user), reply_markup=markup)
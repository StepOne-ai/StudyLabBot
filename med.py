from telebot import types

def oneMed(bot, message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    item1 = types.KeyboardButton("Биоорганическая и биофизическая химия")
    item2 = types.KeyboardButton("Медицинская физика")
    item3 = types.KeyboardButton("Физика, математика")
    item4 = types.KeyboardButton("Химия")
    item5 = types.KeyboardButton("Безопасность жизнедеятельности")
    item6 = types.KeyboardButton("История")
    item7 = types.KeyboardButton("Иностранный язык")
    item8 = types.KeyboardButton("Латинский язык")
    item9 = types.KeyboardButton("Биология")
    item10 = types.KeyboardButton("Анатомия человека")
    item11 = types.KeyboardButton("Первая помощь и уход за больными")
    item12 = types.KeyboardButton("Физическая культура и спорт")
    back = types.KeyboardButton("🔙 Назад 🧫")

    markup.add(item1, item2, item3, item4, 
               item5, item6, item7, item8, item9, item10, item11, item12, back)

    bot.send_message(message.chat.id, '💮 Предмет (листать вниз)'.format(message.from_user), reply_markup=markup)


def twoMed(bot, message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    item1 = types.KeyboardButton("Психология и педагогика")
    item2 = types.KeyboardButton("Биоэтика")
    item3 = types.KeyboardButton("Гистология, эмбриология, цитология")
    item4 = types.KeyboardButton("Биохимия")
    item5 = types.KeyboardButton("Нормальная физиология")
    item6 = types.KeyboardButton("Философия")
    item7 = types.KeyboardButton("Правоведение")
    item8 = types.KeyboardButton("Экономика")
    item9 = types.KeyboardButton("Информатика, медицинская информатика")
    item10 = types.KeyboardButton("Сестринское дело")
    item11 = types.KeyboardButton("Физическая культура и спорт")
    back = types.KeyboardButton("🔙 Назад 🧫")

    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, back)

    bot.send_message(message.chat.id, '💮 Предмет (листать вниз)'.format(message.from_user), reply_markup=markup)


def threeMed(bot, message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    item1 = types.KeyboardButton("Менеджмент")
    item2 = types.KeyboardButton("Микробиология")
    item3 = types.KeyboardButton("Патология")
    item4 = types.KeyboardButton("Лучевая диагностика")
    item5 = types.KeyboardButton("Медицинская генетика")
    item6 = types.KeyboardButton("Фармакология")
    item7 = types.KeyboardButton("Дерматовенерология")
    item8 = types.KeyboardButton("Неврология")
    item9 = types.KeyboardButton("Травматология, ортопедия")
    item10 = types.KeyboardButton("Физическая культура и спорт")

    back = types.KeyboardButton("🔙 Назад 🧫")

    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, back)

    bot.send_message(message.chat.id, '💮 Предмет (листать вниз)'.format(message.from_user), reply_markup=markup)


def fourMed(bot, message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    item1 = types.KeyboardButton("Внутренние болезни")
    item2 = types.KeyboardButton("Хирургические болезни")
    item3 = types.KeyboardButton("Акушерство и гинекология")
    item4 = types.KeyboardButton("Педиатрия")
    item5 = types.KeyboardButton("Оториноларингология")
    item6 = types.KeyboardButton("Психиатрия, медицинская психология")
    item7 = types.KeyboardButton("Клиническая лабораторная диагностика")
    item8 = types.KeyboardButton("Инфекционные болезни")
    item9 = types.KeyboardButton("Фтизиатрия")
    item10 = types.KeyboardButton("Офтальмология")
    item11 = types.KeyboardButton("Стоматология")
    item12 = types.KeyboardButton("Общая гигиена")
    item13 = types.KeyboardButton("Радиационная гигиена")
    item14 = types.KeyboardButton("Физическая культура и спорт")
    back = types.KeyboardButton("🔙 Назад 🧫")

    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13, item14, back)

    bot.send_message(message.chat.id, '💮 Предмет (листать вниз)'.format(message.from_user), reply_markup=markup)


def fiveMed(bot, message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    item1 = types.KeyboardButton("Лидерство")
    item2 = types.KeyboardButton("Административно-правовые основы деятельности врача")
    item3 = types.KeyboardButton("Общественное здоровье и здравоохранение")
    item4 = types.KeyboardButton("Коммунальная гигиена")
    item5 = types.KeyboardButton("Гигиена труда")
    item10 = types.KeyboardButton("Физическая культура и спорт")
    back = types.KeyboardButton("🔙 Назад 🧫")

    markup.add(item1, item2, item3, item4, item5, item10, back)

    bot.send_message(message.chat.id, '💮 Предмет (листать вниз)'.format(message.from_user), reply_markup=markup)


def sixMed(bot, message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    item1 = types.KeyboardButton("Гигиена детей и подростков")
    item2 = types.KeyboardButton("Эпидемиология")
    item3 = types.KeyboardButton("Гигиена питания")
    item11 = types.KeyboardButton("Физическая культура и спорт")
    back = types.KeyboardButton("🔙 Назад 🧫")

    markup.add(item1, item2, item3, item11, back)

    bot.send_message(message.chat.id, '💮 Предмет (листать вниз)'.format(message.from_user), reply_markup=markup)

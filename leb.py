from telebot import types

def oneLeb(bot, message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    item1 = types.KeyboardButton("Науки о жизни")
    item2 = types.KeyboardButton("Техники мышления")
    item3 = types.KeyboardButton("Персональная эффективность")
    item4 = types.KeyboardButton("Основы НИР и проектной деятельности")
    item5 = types.KeyboardButton("Практикум по первой помощи")
    item6 = types.KeyboardButton("Анатомия человека")
    item7 = types.KeyboardButton("Гистология, эмбриология, цитология")
    item8 = types.KeyboardButton("Иностранный язык")
    item9 = types.KeyboardButton("Латинский язык")
    item10 = types.KeyboardButton("История России")
    item11 = types.KeyboardButton("Управление личной безопасностью")
    item12 = types.KeyboardButton("Физика, математика")
    item13 = types.KeyboardButton("Проектный практикум")
    item14 = types.KeyboardButton("Физическая культура и спорт")
    back = types.KeyboardButton("🔙 Назад 🚑")

    markup.add(item1, item2, item3, item4, 
               item5, item6, item7, item8, item9, item10, item11, item12, item13, item14, back)

    bot.send_message(message.chat.id, '💮 Предмет (листать вниз)'.format(message.from_user), reply_markup=markup)


def twoLeb(bot, message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    item1 = types.KeyboardButton("Нормальная физиология")
    item2 = types.KeyboardButton("Биохимия")
    item3 = types.KeyboardButton("Эффективные коммуникации")
    item4 = types.KeyboardButton("Философия")
    item5 = types.KeyboardButton("Экономическая грамотность")
    item6 = types.KeyboardButton("Правовая грамотность")
    item7 = types.KeyboardButton("Сестринское дело")
    item8 = types.KeyboardButton("Микробиология")
    item9 = types.KeyboardButton("Топографическая анатомия и оперативная хирургия")
    item10 = types.KeyboardButton("Организация предпринимательской деятельности")
    item11 = types.KeyboardButton("История медицины и фармации")
    item12 = types.KeyboardButton("Физическая культура и спорт")
    back = types.KeyboardButton("🔙 Назад 🚑")

    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, back)

    bot.send_message(message.chat.id, '💮 Предмет (листать вниз)'.format(message.from_user), reply_markup=markup)


def threeLeb(bot, message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    item1 = types.KeyboardButton("Патологическая анатомия")
    item2 = types.KeyboardButton("Патофизиология")
    item3 = types.KeyboardButton("Пропедевтика внутренних болезней")
    item4 = types.KeyboardButton("Общая Хирургия")
    item5 = types.KeyboardButton("Лучевая диагностика")
    item6 = types.KeyboardButton("Фармакология")
    item7 = types.KeyboardButton("Гигиена")
    item8 = types.KeyboardButton("Общественное здоровье и здравоохранение")
    item9 = types.KeyboardButton("Медицинская генетика")
    item10 = types.KeyboardButton("Иностранный язык для профессионального общения")
    item11 = types.KeyboardButton("IТ-технология и e-health")
    item12 = types.KeyboardButton("Физическая культура и спорт")

    back = types.KeyboardButton("🔙 Назад 🚑")

    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, back)

    bot.send_message(message.chat.id, '💮 Предмет (листать вниз)'.format(message.from_user), reply_markup=markup)


def fourLeb(bot, message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    item1 = types.KeyboardButton("Факультетская терапия")
    item2 = types.KeyboardButton("Факультетская хирургия")
    item3 = types.KeyboardButton("Эндокринология")
    item4 = types.KeyboardButton("Оториноларингология")
    item5 = types.KeyboardButton("Офтальмология")
    item6 = types.KeyboardButton("Неврология, нейрохирургия")
    item7 = types.KeyboardButton("Акушерство и гинекология")
    item8 = types.KeyboardButton("Анестезиология, реаниматология")
    item9 = types.KeyboardButton("Дерматовенерология")
    item10 = types.KeyboardButton("Урология")
    item11 = types.KeyboardButton("Правовое обеспечение профессиональной деятельности")
    item12 = types.KeyboardButton("Иностранный язык для научного общения")
    item13 = types.KeyboardButton("Физическая культура и спорт")
    back = types.KeyboardButton("🔙 Назад 🚑")

    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13, back)

    bot.send_message(message.chat.id, '💮 Предмет (листать вниз)'.format(message.from_user), reply_markup=markup)


def fiveLeb(bot, message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    item1 = types.KeyboardButton("Психиатрия, медицинская психология")
    item2 = types.KeyboardButton("Инфекционные болезни")
    item3 = types.KeyboardButton("Травматология, ортопедия")
    item4 = types.KeyboardButton("Онкология, лучевая терапия")
    item5 = types.KeyboardButton("Акушерство и гинекология")
    item6 = types.KeyboardButton("Госпитальная хирургия")
    item7 = types.KeyboardButton("Фтизиатрия")
    item8 = types.KeyboardButton("Педиатрия")
    item9 = types.KeyboardButton("Доказательная медицина: принцип и методология")
    item10 = types.KeyboardButton("Физическая культура и спорт")
    back = types.KeyboardButton("🔙 Назад 🚑")

    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, back)

    bot.send_message(message.chat.id, '💮 Предмет (листать вниз)'.format(message.from_user), reply_markup=markup)


def sixLeb(bot, message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    item1 = types.KeyboardButton("Медицина чрезвычайных ситуаций")
    item2 = types.KeyboardButton("Челюстио-лицевая хирургия")
    item3 = types.KeyboardButton("Эпидемиология")
    item4 = types.KeyboardButton("Медицинская реабилитология")
    item5 = types.KeyboardButton("Поликлиническое дело")
    item6 = types.KeyboardButton("Клиническая фармакология")
    item7 = types.KeyboardButton("Судебная медицина")
    item8 = types.KeyboardButton("Госпитальная терапия")
    item9 = types.KeyboardButton("Неотложная кардиология")
    item10 = types.KeyboardButton("Трансплантология")
    item11 = types.KeyboardButton("Физическая культура и спорт")
    back = types.KeyboardButton("🔙 Назад 🚑")

    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, back)

    bot.send_message(message.chat.id, '💮 Предмет (листать вниз)'.format(message.from_user), reply_markup=markup)

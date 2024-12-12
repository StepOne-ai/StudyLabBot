from telebot import types

#1131511912 - Мила

def onePedi(bot, message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    item1 = types.KeyboardButton("Науки о жизни")
    item2 = types.KeyboardButton("Техники мышления")
    item3 = types.KeyboardButton("Персональная эффективность")
    item4 = types.KeyboardButton("Основы НИР и проектной деятельности")
    item5 = types.KeyboardButton("Практикум по первой помощи")
    item6 = types.KeyboardButton("Латинский язык")
    item14 = types.KeyboardButton("Физическая культура и спорт")
    back = types.KeyboardButton("🔙 Назад 👶")

    markup.add(item1, item2, item3, item4, 
               item5, item6, item14, back)

    bot.send_message(message.chat.id, '💮 Предмет (листать вниз)'.format(message.from_user), reply_markup=markup)


def twoPedi(bot, message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    item1 = types.KeyboardButton("Анатомия человека с особенностями детского возраста")
    item2 = types.KeyboardButton("Гистология, эмбриология, цитология")
    item3 = types.KeyboardButton("Иностранный язык")
    item4 = types.KeyboardButton("История России")
    item5 = types.KeyboardButton("Управление личной безопасностью")
    item6 = types.KeyboardButton("Эффективные коммуникации")
    item7 = types.KeyboardButton("Нормальная физиология с особенностями детского возраста")
    item8 = types.KeyboardButton("Биохимия")
    item9 = types.KeyboardButton("Сестринское дело")
    item10 = types.KeyboardButton("Философия")
    item11 = types.KeyboardButton("Экономическая грамотность")
    item12 = types.KeyboardButton("Правовая грамотность")
    item13 = types.KeyboardButton("Микробиология, вирусология, иммунология")
    item14 = types.KeyboardButton("Топографичсская анатомия и оперативная хирургия")
    item15 = types.KeyboardButton("Физическая культура и спорт")
    back = types.KeyboardButton("🔙 Назад 👶")

    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13, item14, item15, back)

    bot.send_message(message.chat.id, '💮 Предмет (листать вниз)'.format(message.from_user), reply_markup=markup)


def threePedi(bot, message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    item1 = types.KeyboardButton("Патологическая анатомия")
    item2 = types.KeyboardButton("Патофизиология")
    item3 = types.KeyboardButton("Фармакология")
    item4 = types.KeyboardButton("Пропедевтика внутренних болезней")
    item5 = types.KeyboardButton("Лучевая диагностика")
    item6 = types.KeyboardButton("Общая хирургия")
    item7 = types.KeyboardButton("Гигиена и основы формирования здоровья детей")
    item8 = types.KeyboardButton("Пропедевтика детских болезней")
    item9 = types.KeyboardButton("Дерматовенерология")
    item10 = types.KeyboardButton("Офтальмология")
    item11 = types.KeyboardButton("Оториноларингология")
    item12 = types.KeyboardButton("Физическая культура и спорт")

    back = types.KeyboardButton("🔙 Назад 👶")

    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, back)

    bot.send_message(message.chat.id, '💮 Предмет (листать вниз)'.format(message.from_user), reply_markup=markup)


def fourPedi(bot, message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    item1 = types.KeyboardButton("Внутренние болезни")
    item2 = types.KeyboardButton("Хирургические болезни")
    item3 = types.KeyboardButton("Неврология, нейрохирургия")
    item4 = types.KeyboardButton("Медицина чрезвычайных ситуаций")
    item5 = types.KeyboardButton("IT-технологии и e-health")
    item6 = types.KeyboardButton("Инфекционные болезни")
    item7 = types.KeyboardButton("Психиатрия, медицинская психология")
    item8 = types.KeyboardButton("Фтизиатрия")
    item9 = types.KeyboardButton("Правовое обеспечение профессиональной деятельности")
    item10 = types.KeyboardButton("Травматология, ортопедия")
    item11 = types.KeyboardButton("Факультетская педиатрия")
    item12 = types.KeyboardButton("Иностранный язык для научного общения")
    item13 = types.KeyboardButton("Физическая культура и спорт")
    back = types.KeyboardButton("🔙 Назад 👶")

    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13, back)

    bot.send_message(message.chat.id, '💮 Предмет (листать вниз)'.format(message.from_user), reply_markup=markup)


def fivePedi(bot, message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    item1 = types.KeyboardButton("Факультетская педиатрия")
    item2 = types.KeyboardButton("Детская хирургия")
    item3 = types.KeyboardButton("Медицинская генетика")
    item4 = types.KeyboardButton("Урология")
    item5 = types.KeyboardButton("Эндокринология")
    item6 = types.KeyboardButton("Акушерство и гинекология")
    item7 = types.KeyboardButton("Общественное здоровье и здравоохранение")
    item8 = types.KeyboardButton("Эпидемиология")
    item9 = types.KeyboardButton("Инфекционные болезни у детей")
    item10 = types.KeyboardButton("Физическая культура и спорт")
    back = types.KeyboardButton("🔙 Назад 👶")

    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, back)

    bot.send_message(message.chat.id, '💮 Предмет (листать вниз)'.format(message.from_user), reply_markup=markup)


def sixPedi(bot, message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    item1 = types.KeyboardButton("Клиничсская фармакология")
    item2 = types.KeyboardButton("Госпитальная педиатрия")
    item3 = types.KeyboardButton("Судобная медицина и медицинское право")
    item4 = types.KeyboardButton("Поликлиническая и неотложная педиатрия")
    item5 = types.KeyboardButton("Анестезиология, реаниматология")
    item6 = types.KeyboardButton("Детская онкология, лучевая терапия")
    item7 = types.KeyboardButton("Медицинская реабилитация")
    item8 = types.KeyboardButton("Детская стоматология")
    item11 = types.KeyboardButton("Физическая культура и спорт")
    back = types.KeyboardButton("🔙 Назад 👶")

    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item11, back)

    bot.send_message(message.chat.id, '💮 Предмет (листать вниз)'.format(message.from_user), reply_markup=markup)

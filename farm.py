from telebot import types

def oneFarm(bot, message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    item1 = types.KeyboardButton("Гигиена")
    item2 = types.KeyboardButton("Философия")
    item3 = types.KeyboardButton("Основы профессиональной терминологии.\nЛатинский язык")
    item4 = types.KeyboardButton("Химия биогенных элементов")
    item5 = types.KeyboardButton("Медицинская и биологическая физика")
    item6 = types.KeyboardButton("Анатомия человека")
    item7 = types.KeyboardButton("Физиология")
    item8 = types.KeyboardButton("Органическая химия")
    item9 = types.KeyboardButton("Медицинская биохимия")
    item10 = types.KeyboardButton("Обращение лекарственных средств в России и мире")
    item11 = types.KeyboardButton("История")
    item12 = types.KeyboardButton("Прикладная биостатистика")
    item13 = types.KeyboardButton("Физическая культура и спорт")
    back = types.KeyboardButton("🔙 Назад 🧪")

    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13, back)

    bot.send_message(message.chat.id, '💮 Предмет (листать вниз)'.format(message.from_user), reply_markup=markup)


def twoFarm(bot, message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    item1 = types.KeyboardButton("Физическая культура и спорт")
    item2 = types.KeyboardButton("Молекулярная биология")
    item3 = types.KeyboardButton("Оценка функционального состояния\nорганизма человека")
    item4 = types.KeyboardButton("Основы биоинформатики и дизайна лекарственных средств")
    item5 = types.KeyboardButton("Биоэтика")
    item6 = types.KeyboardButton("Медицинская генетика")
    item7 = types.KeyboardButton("Профессиональный иностранный язык")
    item8 = types.KeyboardButton("Патология")
    item9 = types.KeyboardButton("Микробиология")
    item10 = types.KeyboardButton("Физическая и коллоидния химия")
    item11 = types.KeyboardButton("История медицины и фармации")
    item12 = types.KeyboardButton("Безопасность жизнедеятельности")
    item13 = types.KeyboardButton("Ботаника")
    back = types.KeyboardButton("🔙 Назад 🧪")

    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9,
                item10, item11, item12, item13, back)

    bot.send_message(message.chat.id, '💮 Предмет (листать вниз)'.format(message.from_user), reply_markup=markup)


def threeFarm(bot, message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    item1 = types.KeyboardButton("Аналитическая химия")
    item2 = types.KeyboardButton("ФАРМАЦИЯ")
    item3 = types.KeyboardButton("Общая фармацевтическая химия")
    item4 = types.KeyboardButton("Методы фармакопейного анализа")
    item5 = types.KeyboardButton("Фармакоэпидемиология")
    item6 = types.KeyboardButton("Медицинское и фармацевтическое \nтовароведение")
    item7 = types.KeyboardButton("Фармакогнозия")
    item8 = types.KeyboardButton("Общая фармацевтическая технология")
    item9 = types.KeyboardButton("Физическая культура и спорт")
    back = types.KeyboardButton("🔙 Назад 🧪")

    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, back)

    bot.send_message(message.chat.id, '💮 Предмет (листать вниз)'.format(message.from_user), reply_markup=markup)


def fourFarm(bot, message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    item1 = types.KeyboardButton("Основы разработки и производства\n иммунобиологичсских лекарственных \nпрепаратов")
    item2 = types.KeyboardButton("Надлежащие практики в \nобращении лекарственных средств")
    item3 = types.KeyboardButton("Фармацевтический маркетинг")
    item4 = types.KeyboardButton("Биофармация")
    item5 = types.KeyboardButton("Управление и экономика фармации")
    item6 = types.KeyboardButton("Основы биотехнологии")
    item7 = types.KeyboardButton("Лекарственные средства\n из природного сырья")
    item8 = types.KeyboardButton("Молекулярные основы действия\n лекарственных средств")
    item9 = types.KeyboardButton("Фармакотерапия")
    item10 = types.KeyboardButton("Фармацевтическая экология")
    item11 = types.KeyboardButton("Физическая культура и спорт")
    back = types.KeyboardButton("🔙 Назад 🧪")

    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, back)

    bot.send_message(message.chat.id, '💮 Предмет (листать вниз)'.format(message.from_user), reply_markup=markup)


def fiveFarm(bot, message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    item1 = types.KeyboardButton("Специальная фармацевтическая Химия")
    item2 = types.KeyboardButton("Частная фармацевтическия технология")
    item3 = types.KeyboardButton("Фармацевтичсское информирование")
    item4 = types.KeyboardButton("Фармацевтичсский менеджмент")
    item5 = types.KeyboardButton("Фармацевтическая логистика")
    item6 = types.KeyboardButton("Юридические основы деятельности провизора")
    item7 = types.KeyboardButton("Первая помощь при неотложных состояниях")
    item8 = types.KeyboardButton("Физическая культура и спорт")
    back = types.KeyboardButton("🔙 Назад 🧪")

    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, back)

    bot.send_message(message.chat.id, '💮 Предмет (листать вниз)'.format(message.from_user), reply_markup=markup)

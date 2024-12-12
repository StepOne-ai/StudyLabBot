from telebot import types

def backFarm(bot, message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("1️⃣🧪")
    item2 = types.KeyboardButton("2️⃣🧪")
    item3 = types.KeyboardButton("3️⃣🧪")
    item4 = types.KeyboardButton("4️⃣🧪")
    item5 = types.KeyboardButton("5️⃣🧪")
    back = types.KeyboardButton("🔙 Назад")

    markup.add(item1, item2, item3, item4, item5, back)

    bot.send_message(message.chat.id, '💮 Выберите курс, на котором будет сдача экзамена'.format(message.from_user), reply_markup=markup)

def backLeb(bot, message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("1️⃣🚑")
    item2 = types.KeyboardButton("2️⃣🚑")
    item3 = types.KeyboardButton("3️⃣🚑")
    item4 = types.KeyboardButton("4️⃣🚑")
    item5 = types.KeyboardButton("5️⃣🚑")
    item6 = types.KeyboardButton("6️⃣🚑")
    back = types.KeyboardButton("🔙 Назад")

    markup.add(item1, item2, item3, item4, item5, item6, back)

    bot.send_message(message.chat.id, '💮 Выберите курс, на котором будет сдача экзамена'.format(message.from_user), reply_markup=markup)

def backMed(bot, message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("1️⃣🧫")
    item2 = types.KeyboardButton("2️⃣🧫")
    item3 = types.KeyboardButton("3️⃣🧫")
    item4 = types.KeyboardButton("4️⃣🧫")
    item5 = types.KeyboardButton("5️⃣🧫")
    item6 = types.KeyboardButton("6️⃣🧫")
    back = types.KeyboardButton("🔙 Назад")

    markup.add(item1, item2, item3, item4, item5, item6, back)
    
    bot.send_message(message.chat.id, '💮 Выберите курс, на котором будет сдача экзамена'.format(message.from_user), reply_markup=markup)

def backPedi(bot, message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("1️⃣👶")
    item2 = types.KeyboardButton("2️⃣👶")
    item3 = types.KeyboardButton("3️⃣👶")
    item4 = types.KeyboardButton("4️⃣👶")
    item5 = types.KeyboardButton("5️⃣👶")
    item6 = types.KeyboardButton("6️⃣👶")
    back = types.KeyboardButton("🔙 Назад")

    markup.add(item1, item2, item3, item4, item5, item6, back)

    bot.send_message(message.chat.id, '💮 Выберите курс, на котором будет сдача экзамена'.format(message.from_user), reply_markup=markup)

def backStom(bot, message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("1️⃣🦷")
    item2 = types.KeyboardButton("2️⃣🦷")
    item3 = types.KeyboardButton("3️⃣🦷")
    item4 = types.KeyboardButton("4️⃣🦷")
    item5 = types.KeyboardButton("5️⃣🦷")
    back = types.KeyboardButton("🔙 Назад")

    markup.add(item1, item2, item3, item4, item5, back)

    bot.send_message(message.chat.id, '💮 Выберите курс, на котором будет сдача экзамена'.format(message.from_user), reply_markup=markup)

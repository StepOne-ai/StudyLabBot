import telebot
from telebot import types
import farm
import leb
import med
import pedi
import stom
import manager
import backs
import data
import db

bot = telebot.TeleBot('7087891015:AAF62foh7kXYJrgu5fIcYK1wwLRBypYJjE');

users = db.get_all("visits")

@bot.message_handler(commands=['start'])
def start(message):
    yes = True
    for user in users:
        try:
            if user.get('id') == message.from_user.id:
                yes = False
        except:
            yes = True
    
    if yes:
        if db.push({"id": message.from_user.id, "username": message.from_user.username}, "visits") == True:
             print("Данные успешно добавлены")
        else:
            print("Ошибка при добавлении данных")
            
    text = f"Вас приветствует команда StudyLab. 🐍\n\n" \
           f"Наш бот поможет Вам в поиске и приобретении любых работ для ПМГМУ им. И.М. Сеченова. ⚕️\n\n" \
           f"Свяжитесь с нами, и любая Ваша проблема решится 🔮\n\n"\
           f"Для личной заявки нажмите '🎩 МЕНЕДЖЕР'\n\n"


    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    webAppTest = types.WebAppInfo("https://testdb-xi.vercel.app/med")
    item1 = types.KeyboardButton('🧪 ФАРМАЦИЯ')
    item2 = types.KeyboardButton('🚑 ЛЕЧЕБНОЕ ДЕЛО')
    item3 = types.KeyboardButton('🧫 МЕДИКО-ПРОФИЛАКТИЧЕСКОЕ ДЕЛО')
    item4 = types.KeyboardButton('🦷 СТОМАТОЛОГИЯ')
    item5 = types.KeyboardButton('👶 ПЕДИАТРИЯ')
    item6 = types.KeyboardButton('🎩 МЕНЕДЖЕР')
    item7 = types.KeyboardButton('🔊FAQ')
    item8 = types.KeyboardButton(text='📞ОСТАВИТЬ ОТЗЫВ', web_app=webAppTest)
    items = [item1, item2, item3, item4, item5, item6, item7, item8]
    keyboard.add(*items)
    bot.send_photo(message.chat.id, photo=open("opening.png", "rb"), caption=text, reply_markup=keyboard)
    # bot.send_message(message.chat.id, "!!! В данный момент ведутся профилактические работы, бот может не работать, смотрите описание бота!!!")

    # Меню Факультетов
    # markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #row_width ...
    # item1 = types.KeyboardButton("Привет")
    # item2 = types.KeyboardButton("Пока")

    # markup.add(item1, item2)

    # bot.send_message(message.chat.id, 'Привет {0.first_name}!'.format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "🧪 ФАРМАЦИЯ":

        data.fac = "FARM"
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("1️⃣🧪")
        item2 = types.KeyboardButton("2️⃣🧪")
        item3 = types.KeyboardButton("3️⃣🧪")
        item4 = types.KeyboardButton("4️⃣🧪")
        item5 = types.KeyboardButton("5️⃣🧪")
        back = types.KeyboardButton("🔙 Назад")

        markup.add(item1, item2, item3, item4, item5, back)

        bot.send_message(message.chat.id, '💮 Выберите курс, на котором будет сдача экзамена'.format(message.from_user), reply_markup=markup)
    elif message.text == "🚑 ЛЕЧЕБНОЕ ДЕЛО":
        data.fac = "LEB"
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
    elif message.text == "🧫 МЕДИКО-ПРОФИЛАКТИЧЕСКОЕ ДЕЛО":

        data.fac = "MED"
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
    elif message.text == "👶 ПЕДИАТРИЯ":

        data.fac = "PEDI"
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
    elif message.text == "🦷 СТОМАТОЛОГИЯ":

        data.fac = "STOM"
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("1️⃣🦷")
        item2 = types.KeyboardButton("2️⃣🦷")
        item3 = types.KeyboardButton("3️⃣🦷")
        item4 = types.KeyboardButton("4️⃣🦷")
        item5 = types.KeyboardButton("5️⃣🦷")
        back = types.KeyboardButton("🔙 Назад")

        markup.add(item1, item2, item3, item4, item5, back)

        bot.send_message(message.chat.id, '💮 Выберите курс, на котором будет сдача экзамена'.format(message.from_user), reply_markup=markup)
    elif message.text == "🔙 Назад":

        data.fac = ""
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        webAppTest = types.WebAppInfo("https://testdb-xi.vercel.app/med")
        item1 = types.KeyboardButton('🧪 ФАРМАЦИЯ')
        item2 = types.KeyboardButton('🚑 ЛЕЧЕБНОЕ ДЕЛО')
        item3 = types.KeyboardButton('🧫 МЕДИКО-ПРОФИЛАКТИЧЕСКОЕ ДЕЛО')
        item4 = types.KeyboardButton('🦷 СТОМАТОЛОГИЯ')
        item5 = types.KeyboardButton('👶 ПЕДИАТРИЯ')
        item6 = types.KeyboardButton('🎩 МЕНЕДЖЕР')
        item7 = types.KeyboardButton('🔊FAQ')
        item8 = types.KeyboardButton(text='📞ОСТАВИТЬ ОТЗЫВ', web_app=webAppTest)
        items = [item1, item2, item3, item4, item5, item6, item7, item8]
        keyboard.add(*items)

        bot.send_message(message.chat.id, '💮 Выберите факультет'.format(message.from_user), reply_markup=keyboard)
    elif message.text == "🔙 Назад 🧪":
        data.course = 0
        backs.backFarm(bot, message)
    elif message.text == "🔙 Назад 🚑":
        data.course = 0
        backs.backLeb(bot, message)
    elif message.text == "🔙 Назад 🧫":
        data.course = 0
        backs.backMed(bot, message)
    elif message.text == "🔙 Назад 👶":
        data.course = 0
        backs.backPedi(bot, message)
    elif message.text == "🔙 Назад 🦷":
        data.course = 0
        backs.backStom(bot, message)
    elif message.text == "1️⃣🧪":

        data.course = 1
        farm.oneFarm(bot, message)
    elif message.text == "2️⃣🧪":

        data.course = 2
        farm.twoFarm(bot, message)
    elif message.text == "3️⃣🧪":

        data.course = 3
        farm.threeFarm(bot, message)
    elif message.text == "4️⃣🧪":

        data.course = 4
        farm.fourFarm(bot, message)
    elif message.text == "5️⃣🧪":

        data.course = 5
        farm.fiveFarm(bot, message)
    elif message.text == "1️⃣🚑":

        data.course = 1
        leb.oneLeb(bot, message)
    elif message.text == "2️⃣🚑":

        data.course = 2
        leb.twoLeb(bot, message)
    elif message.text == "3️⃣🚑":

        data.course = 3
        leb.threeLeb(bot, message)
    elif message.text == "4️⃣🚑":

        data.course = 4
        leb.fourLeb(bot, message)
    elif message.text == "5️⃣🚑":

        data.course = 5
        leb.fiveLeb(bot, message)
    elif message.text == "6️⃣🚑":

        data.course = 6
        leb.sixLeb(bot, message)
    elif message.text == "1️⃣🧫":
        data.course = 1
        med.oneMed(bot, message)
    elif message.text == "2️⃣🧫":
        data.course = 2
        med.twoMed(bot, message)
    elif message.text == "3️⃣🧫":
        data.course = 3
        med.threeMed(bot, message)
    elif message.text == "4️⃣🧫":
        data.course = 4
        med.fourMed(bot, message)
    elif message.text == "5️⃣🧫":
        data.course = 5
        med.fiveMed(bot, message)
    elif message.text == "6️⃣🧫":
        data.course = 6
        med.sixMed(bot, message)
    elif message.text == "1️⃣👶":
        data.course = 1
        pedi.onePedi(bot, message)
    elif message.text == "2️⃣👶":
        data.course = 2
        pedi.twoPedi(bot, message)
    elif message.text == "3️⃣👶":
        data.course = 3
        pedi.threePedi(bot, message)
    elif message.text == "4️⃣👶":
        data.course = 4
        pedi.fourPedi(bot, message)
    elif message.text == "5️⃣👶":
        data.course = 5
        pedi.fivePedi(bot, message)
    elif message.text == "6️⃣👶":
        data.course = 6
        pedi.sixPedi(bot, message)
    elif message.text == "1️⃣🦷":
        data.course = 1
        stom.oneStom(bot, message)
    elif message.text == "2️⃣🦷":
        data.course = 2
        stom.twoStom(bot, message)
    elif message.text == "3️⃣🦷":
        data.course = 3
        stom.threeStom(bot, message)
    elif message.text == "4️⃣🦷":
        data.course = 4
        stom.fourStom(bot, message)
    elif message.text == "5️⃣🦷":
        data.course = 5
        stom.fiveStom(bot, message)
    elif message.text == "🎩 МЕНЕДЖЕР":
        manager.manager(bot, message)
    elif message.text == "Оставить заявку на личный вопрос":
        data.type = "dm"
        ask(message)
    elif message.text == "Письменная отработка":
        data.work_type = message.text
        ask(message)
    elif message.text == "Письменное  домашнее задание":
        data.work_type = message.text
        ask(message)
    elif message.text == "Написание тетради":
        data.work_type = message.text
        ask(message)
    elif message.text == "Презентация":
        data.work_type = message.text
        ask(message)
    elif message.text == "Реферат/доклад":
        data.work_type = message.text
        ask(message)
    elif message.text == "Решение тестов(ЭОР)":
        data.work_type = message.text
        ask(message)
    elif message.text == "Репетиторство":
        data.work_type = message.text
        ask(message)
    elif message.text == "🔊FAQ":
        bot.send_message(message.chat.id, "🔊FAQ🔊\n\nКак осуществляется оплата ?\n\nНа карту. Предоплата 50% , 50% при получении услуги.")
        bot.send_message(message.chat.id, "Через сколько ответит менеджер ?\n\nОт 10 минут до 3 часов ")
        bot.send_message(message.chat.id, "Кто осуществляет работу ? \n\n Наша команда состоит из большого количества узкопрофильный специалистов, которые качественно выполнят работу.")
        bot.send_message(message.chat.id, "О нас : \n\n StudyLab-это образовательная платформа для помощи студентам ПМГМУ. С 2020 года мы способствуем облегчению учебного процесса. ")
        bot.send_message(message.chat.id, "Акции и скидки ? \n\nМы всегда рады долгосрочному сотрудничеству, поэтому предоставляем скидки. Подробную информацию вам предоставит наш менеджер")
        bot.send_message(message.chat.id, "По другим вопросам вас проконсультирует менеджер")
    elif message.text == "📞ОСТАВИТЬ ОТЗЫВ":
        markup_inline = types.InlineKeyboardMarkup(row_width=1)
        webAppTest = types.WebAppInfo("https://testdb-xi.vercel.app/med")
        item = types.InlineKeyboardButton(
            text='📞💆🏾‍♂️', web_app=webAppTest)
        markup_inline.add(item)
        keyboard = types.ReplyKeyboardMarkup(row_width=1)
        one_butt = types.KeyboardButton(text="ОСТАВИТЬ КОММЕНТАРИЙ", web_app=webAppTest) #создаем кнопку типа webapp
        keyboard.add(one_butt) #добавляем кнопки в клавиатуру
        bot.send_message( message.chat.id, 'Нажмите на кнопку чтобы оставить комментарий', reply_markup=markup_inline)
    else:
        if data.fac != "" and data.course != 0:
            data.work = message.text
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            item1 = types.KeyboardButton("Письменная отработка")
            item2 = types.KeyboardButton("Написание тетради")
            item3 = types.KeyboardButton("Письменное домашнее задание")
            item4 = types.KeyboardButton("Презентация")
            item5 = types.KeyboardButton("Реферат/доклад")
            item6 = types.KeyboardButton("Решение тестов(ЭОР)")
            item7 = types.KeyboardButton("Репетиторство")
            back = types.KeyboardButton("🔙 Назад")

            markup.add(item1, item2, item3, item4, item5, item6, item7, back)

            bot.send_message(message.chat.id, 'Продолжим...', reply_markup=markup)
def get_comment(message):
    if message.text != "🔙 Назад":
        data.comment = message.text
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        item1 = types.KeyboardButton("🔙 Назад")
        markup.add(item1)
        if data.type != "dm":
            manager.send_all(bot, 510443335, message) #6334935563
            manager.send_all(bot, 6334935563, message)
            data.type = ""
        else:
            manager.send_data(bot, 510443335, message)
            manager.send_data(bot, 6334935563, message)
            data.type = ""
        bot.send_message(message.chat.id, "Заявка успешно отправлена, оператор свяжется с вами в ближайшее время!", reply_markup=markup)
    else:
        data.fac = ""
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        webAppTest = types.WebAppInfo("https://testdb-xi.vercel.app/med")
        item1 = types.KeyboardButton('🧪 ФАРМАЦИЯ')
        item2 = types.KeyboardButton('🚑 ЛЕЧЕБНОЕ ДЕЛО')
        item3 = types.KeyboardButton('🧫 МЕДИКО-ПРОФИЛАКТИЧЕСКОЕ ДЕЛО')
        item4 = types.KeyboardButton('🦷 СТОМАТОЛОГИЯ')
        item5 = types.KeyboardButton('👶 ПЕДИАТРИЯ')
        item6 = types.KeyboardButton('🎩 МЕНЕДЖЕР')
        item7 = types.KeyboardButton('🔊FAQ')
        item8 = types.KeyboardButton(text='📞ОСТАВИТЬ ОТЗЫВ', web_app=webAppTest)
        items = [item1, item2, item3, item4, item5, item6, item7, item8]
        keyboard.add(*items)

        bot.send_message(message.chat.id, '💮 Выберите факультет'.format(message.from_user), reply_markup=keyboard)

def ask(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    item1 = types.KeyboardButton("🔙 Назад")
    item2 = types.KeyboardButton("Без комментариев")
    markup.add(item2, item1)
    bot.send_message(message.chat.id, "Напишите комментарий по заказу (Опционально)", reply_markup=markup)
    bot.register_next_step_handler(message, get_comment);

print("Bot is running...")
bot.infinity_polling(timeout=10, long_polling_timeout = 5)

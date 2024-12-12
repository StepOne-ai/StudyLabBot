from telebot import types
import data

def manager(bot, message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    item1 = types.KeyboardButton("Оставить заявку на личный вопрос")
    back = types.KeyboardButton("🔙 Назад")

    markup.add(item1, back)
    #message.from_user.username
    bot.send_message(message.chat.id, text="Вы можете оставить заявку на получение консультации", reply_markup=markup)

def send_data(bot, chat_id, message):
    bot.send_message(chat_id, f"Оператор, пришла личная заявка от @{message.chat.username}\nСсылка: https://t.me/@id{message.from_user.id}\nКомментарий: {data.comment}")
def send_all(bot, chat_id, message):
    bot.send_message(chat_id, f"Оператор, вам пришла заявка от\nЗаказчик: @{message.chat.username}\nСсылка: https://t.me/@id{message.from_user.id}\nФакультет: {data.fac}\nКурс: {data.course}\nДисциплина: {data.work}\nТип работы: {data.work_type}\nКомментарий: {data.comment}")
# import telebot
#
#
# bot = telebot.TeleBot('350404818:AAFktEZ0gt6MCpqZ78CbM0DS5XyYYH7faOs')
#
#
# def start_menu():
#     user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
#     user_markup.row('Регистрация')
#     user_markup.row('Чат')
#     user_markup.row('Программа')
#     user_markup.row('Контакты')
#     return user_markup
#
#
# def program_menu():
#     user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
#     user_markup.row('Начало')
#     user_markup.row('Перерыв')
#     user_markup.row('Вторая часть')
#     user_markup.row('Конец')
#     return user_markup
#
#
# @bot.message_handler(commands=['start'])
# def handle_start(message):
#     bot.send_message(message.from_user.id, 'Драсти', reply_markup=start_menu())
#
#
# @bot.message_handler(content_types=['text'])
# def handle_text(message):
#     if message.text == "Программа":
#         bot.send_message(message.from_user.id, 'Расписание программы :)', reply_markup=program_menu())
#
#
# bot.polling(none_stop=True)
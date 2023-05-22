import telebot
from telebot import types
from DataBase import Commands

class Bot():
    def __init__(self, token):
        
        self.bot = telebot.TeleBot(token, parse_mode="MarkDown")
        self.data_base = Commands()

    def create_keyboard_class(self, message, user_name, user_id):
        # Создаем объект клавиатуры
        keyboard = types.InlineKeyboardMarkup(row_width=2)

        # Создаем кнопки
        button1 = types.InlineKeyboardButton('Я в 9 классе (ОГЭ)', callback_data=f'9.{user_name}.{user_id}', switch_inline_query_current_chat='')
        button2 = types.InlineKeyboardButton('Я в 11 классе (ЕГЭ)', callback_data=f'11.{user_name}.{user_id}', switch_inline_query_current_chat='')
        keyboard.add(button1, button2)

        self.bot.send_message(message.chat.id, "К какому экзамену вы готовитесь?", reply_markup=keyboard)

    # for add new lesson in data base
    def create_keyboard_lessons(self):
        pass

    def run(self):
        @self.bot.message_handler(commands=["start"], content_types=["text"])
        def start_message(message):
            user_name = message.from_user.username
            user_id = message.from_user.id

            self.bot.send_message(message.chat.id, "Привет")
            self.create_keyboard_class(message, user_name, user_id)


        # <------------ Listenning messages ------------>

        @self.bot.callback_query_handler(func=lambda call: True)
        def listen_button_call(call):
            data = call.data.split(".")
            self.data_base.add_new_user(user_name = data[1],
                                        user_id = data[2],
                                        user_class = int(data[0]))
            self.bot.send_message(call.chat.id, "Отлично, теперь выбирите предметы, которые планируете сдавать:")
            self.create_keyboard_lesson()

        
        # <-------------- Starting the bot --------------------->
        self.bot.polling(none_stop=True)


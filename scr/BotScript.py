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
    def create_keyboard_lessons(self, message):
        # Создаем объект клавиатуры
        keyboard = types.InlineKeyboardMarkup(row_width=2)

        # Создаем кнопки
        button1 = types.InlineKeyboardButton('Английский язык', callback_data=f'lesson.english', switch_inline_query_current_chat='')
        button2 = types.InlineKeyboardButton('Математика', callback_data=f'lesson.mathematics', switch_inline_query_current_chat='')
        button3 = types.InlineKeyboardButton('Русский язык', callback_data=f'lesson.russian', switch_inline_query_current_chat='')
        button4 = types.InlineKeyboardButton('Информатика', callback_data=f'lesson.informatika', switch_inline_query_current_chat='')
        button5 = types.InlineKeyboardButton('Физика', callback_data=f'lesson.physics', switch_inline_query_current_chat='')
        button6 = types.InlineKeyboardButton('География', callback_data=f'lesson.geography', switch_inline_query_current_chat='')

        keyboard.add(button1, button2)
        keyboard.add(button3, button4)
        keyboard.add(button5, button6)

        self.bot.send_message(message.chat.id, "К какому экзамену вы готовитесь?", reply_markup=keyboard)


    def create_keyboard_lessons_study(self, message):
        user_id = message.from_user.id
        self.data_base.search_data(user_id)


    def run(self):
        @self.bot.message_handler(commands=["start"], content_types=["text"])
        def start_message(message):
            user_name = message.from_user.username
            user_id = message.from_user.id

            self.bot.send_message(message.chat.id, "Привет")
            self.create_keyboard_class(message, user_name, user_id)


        @self.bot.message_handler(commands=["add"], content_types=["text"])
        def add_lesson_message(message):
            self.bot.send_message(message.chat.id, "Выбирай")
            self.create_keyboard_lessons(message)


        @self.bot.message_handler(commands=["study"], content_types=["text"])
        def start_lesson_message(message):
            
            self.bot.send_message(message.chat.id, "ОК")
            self.create_keyboard_lessons_study(message)


        # <------------ Listenning messages ------------>

        @self.bot.callback_query_handler(func=lambda call: True)
        def listen_button_call(call):
            data = call.data.split(".")
            if data[0]=="9" or data[0]=="11":
                self.data_base.add_new_user(user_name = data[1],
                                            user_id = data[2],
                                            user_class = int(data[0]))
                self.bot.send_message(call.from_user.id, "Отлично, чтобы добавить предмет для подготовки, используйте /add")

            elif data[0]=="lesson":
                self.data_base.add_new_lessons(call.from_user.id, data[1])
                self.bot.send_message(call.from_user.id, "Предмет добавлен! Чтобы начать подготовку, используйте /study")


        
        # <-------------- Starting the bot --------------------->
        self.bot.polling(none_stop=True)


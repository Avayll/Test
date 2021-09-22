import telebot
from telebot.types import InlineKeyboardMarkup, Message
from telebot import types

token = "1976579476:AAErpiOR1KSnBUedtHsEOl5xaVrNSrc-XNM"

bot = telebot.TeleBot(token)

BOT_CONFIG = {
    "Tasks" : {
        "Сегодня" : ["123", "поесть", "посрать"]
    }
}

@bot.message_handler(commands=["start"])
def Welcome(message):

    HELP = 'Приветствую вас, это бот задачник, что вы хотите сделать?'
    #Создаем переменную markup_inline = types.InlineKeyboardMarkup()
    #И уже с помощью команд под ней создаем кнопки с колбек датой и текстом на кнопке
    markup_inline = types.InlineKeyboardMarkup()
    button_create = types.InlineKeyboardButton(text="Создать задачу", callback_data="create")
    button_delete = types.InlineKeyboardButton(text="Удалить список задач", callback_data="delete")
    button_show = types.InlineKeyboardButton(text="Показать список задач", callback_data="show")
    button_random = types.InlineKeyboardButton(text="Секретная команда", callback_data="random")

    #А вот тут вставляем эти кнопки в переменную markup_inline чтобы они были, без строк ниже кнопок не будет
    #Тем более ниже сообщение на которое инлайн кнопки прикрепятся, а в параметрах этого сообщения надо как раз таки вставить переменную с кнопками
    markup_inline.add(button_create, button_delete, button_random, button_show)
    bot.send_message(message.chat.id, HELP, 
        reply_markup = markup_inline
    )

@bot.callback_query_handler(func = lambda call: True)
def MainCall(call):
    if call.data == "show":
        show(call)
    elif call.data == "random":
        RickRoll()
    elif call.data == "create":
        add(call)
    elif call.data == "delete":
        delete(call)
    else:
        bot.send_message(call.message.chat.id, "Ошибка")

#ФФункция показывающая список
def show(call):
    show_message = bot.send_message(call.message.chat.id, "На какую дату вы хотите посмотреть задачи?")
    bot.register_next_step_handler(show_message, show1)

def show1(message):
    date = message.text
    show_message = bot.send_message(message.chat.id, "Принято")
    show_func(show_message, date)
    
def show_func(message, date):
    if date in BOT_CONFIG["Tasks"]:
        acum = "\n- ".join(BOT_CONFIG["Tasks"][date])
        if "https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=PLxb0XwjhqM_RLETkiOkUZrEE8K-fP3V-p&index=2" in acum:
            bot.send_video(message.chat.id, 'https://i.imgflip.com/1mfn7l.gif', None, 'Never Gonna Give you up')
        else:
            bot.send_message(message.chat.id, "- " + acum)
    elif date not in BOT_CONFIG["Tasks"]:
        bot.send_message(message.chat.id, "Извините, задач на такую дату нет")

#Секретная команда
def RickRoll():
    Ricky = "https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=PLxb0XwjhqM_RLETkiOkUZrEE8K-fP3V-p&index=2"
    BOT_CONFIG["Tasks"]["Сегодня"].append(Ricky)

#Удаляющая функция
def delete(call):
    delete_message = bot.send_message(call.message.chat.id, "На какую дату хотите очистить список?")
    bot.register_next_step_handler(delete_message, delete1)

def delete1(message):
    delete_answer = message.text
    if delete_answer in BOT_CONFIG["Tasks"]:
        del BOT_CONFIG["Tasks"][delete_answer]
        BOT_CONFIG["Tasks"][delete_answer] = []
    else:
        bot.send_message(message.chat.id, "Такой даты не существует в списке.")

#Создающая функция
def add(call):
    first_message = bot.send_message(call.message.chat.id, "На какое число хотите создать задачу?")
    bot.register_next_step_handler(first_message, tranzit)

def tranzit(message):
    first_message = message.text
    second_name = bot.send_message(message.chat.id, "А какую задачу?")
    bot.register_next_step_handler(second_name, tranzit1, first_message)

def tranzit1(message, first_message):
    second_name = message.text
    print(first_message, second_name)
    AddFunc(first_message, second_name)

def AddFunc(date, task):
    if date in BOT_CONFIG["Tasks"]:
        BOT_CONFIG["Tasks"][date].append(task)
    else:
        BOT_CONFIG["Tasks"][date] = [task]
    print(BOT_CONFIG["Tasks"][date])

bot.polling(none_stop=True)
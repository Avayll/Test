from re import X
import telebot
from telebot.types import Message
#import random
token = "1976579476:AAErpiOR1KSnBUedtHsEOl5xaVrNSrc-XNM"

bot = telebot.TeleBot(token)

HELP = '''Приветствую, чтобы создать задачу скажите "/Создать"
Если хотите посмотреть задачу то скажите "/Посмотреть"
Если хотите получить рандомную задачу себе на сегодня то напишите "/random"
Если хотите очистить список задач на какую либо дату напишите "/Удалить"'''

BOT_CONFIG = {
    "Tasks" : {
        "Сегодня" : ["123", "поесть", "посрать"]
    }
}



@bot.message_handler(commands=["start"])
def Welcome(message):
    bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands=["Посмотреть", "Показать"])
def show(message):
    show_message = bot.send_message(message.chat.id, "На какую дату вы хотите посмотреть задачи?")
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

@bot.message_handler(commands=["random"])
def RickRoll(Ricky):
    Ricky = "https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=PLxb0XwjhqM_RLETkiOkUZrEE8K-fP3V-p&index=2"
    BOT_CONFIG["Tasks"]["Сегодня"].append(Ricky)

@bot.message_handler(commands=["Удалить"])
def delete(message):
    delete_message = bot.send_message(message.chat.id, "На какую дату хотите очистить список?")
    bot.register_next_step_handler(delete_message, delete1)

def delete1(message):
    delete_answer = message.text
    if delete_answer in BOT_CONFIG["Tasks"]:
        del BOT_CONFIG["Tasks"][delete_answer]
        BOT_CONFIG["Tasks"][delete_answer] = []
    else:
        bot.send_message(message.chat.id, "Такой даты не существует в списке.")

@bot.message_handler(commands=["Создать"])
def add(message):
    first_message = bot.send_message(message.chat.id, "На какое число хотите создать задачу?")
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
import telebot
#import random
token = "1976579476:AAErpiOR1KSnBUedtHsEOl5xaVrNSrc-XNM"

bot = telebot.TeleBot(token)

HELP = '''Приветствую, чтобы создать задачу скажите "/Создать задачу"
Если хотите посмотреть задачу то скажите "/Посмотреть"
Если хотите получить рандомную задачу себе на сегодня то напишите " /Хочу рандомную задачу"'''

BOT_CONFIG = {
    "Tasks" : {
        "Сегодня" : []
    },
    "RandomTasks" : ["RickRoll"]
}



@bot.message_handler(commands=["start"])
def Welcome(message):
    bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands=["Посмотреть", "Показать"])
def show(message):
    message_need1 = "На какую дату хотите узнать задачу?"
    MoreStep(message, message_need1)
    # if data1 in BOT_CONFIG["Tasks"]:
    #     for FinalTasks in 
            #bot.send_message(message.chat.id, FinalTasks)
    
@bot.message_handler(commands=["Создать"])
def add(message):
    data1 = ""
    data2 = ""
    message_need1 = "На какое число хотите задать задачу?"
    message_need2 = "А какую задачу?"
    MoreStep(message, message_need1, message_need2, data1, data2)
    date = data1
    task = data2
    AddFunc(date, task)

def AddFunc(date, task):
    if date in BOT_CONFIG["Tasks"]:
        BOT_CONFIG["Tasks"][date].append(task)
    else:
        BOT_CONFIG["Tasks"][date] = [task]


def MoreStep(message, message_need1, message_need2, data1, data2):
    data1 = ""
    data2 = ""
    task1 = bot.send_message(message.chat.id, message_need1)
    bot.register_next_step_handler(task1, MoreStep1, message_need2)
    return data1, data2

def MoreStep1(message, message_need2):
    data2 = message.text
    data1 = bot.send_message(message.chat.id, message_need2)
    bot.register_next_step_handler(message, MoreStep2, data1, data2)

def MoreStep2(message, data2, data1):
    data2 = message.text
    print(data1, data2)
    return data1, data2


#def MoreStep(message, user_message, message_need):
    #user_message = bot.send_message(message.chat.id, message_need)
    #MoreStep_Tranzit()
    #MoreStep_FinalData

#def MoreStep_Tranzit(message, message_need1):
    #Data1 = bot.send_message(message.chat.id, message_need1)
    #bot.register_next_step_handler(Data1, MoreStep_FinalData)

#def MoreStep_FinalData(message, message_need2):
    #Data2 = bot.send_message(message.chat.id, message_need2)


#def start(message):
    #msg = bot.send_message(message.chat.id, 'Введите первое значение')
    #bot.register_next_step_handler(msg, start_2)


#def start_2(message):
   # msg = bot.send_message(message.chat.id, 'Введите второе значение')
    #bot.register_next_step_handler(msg, start_3, message.text)


#def start_3(message, value):
    #print(message.text, value)

bot.polling(none_stop=True)

import telebot
import random
import config
import logger as log

bot = telebot.TeleBot(config.CALC_BOT_TOKEN)


@bot.message_handler(commands=['help'])
def description(message):
    log.logger("Пользователь "+ message.from_user.first_name + " запустил /help",message.from_user.id, message.from_user.first_name, message.from_user.username)
    bot.send_message(message.chat.id, "Введите математическое выражение. Например (2+2)*2")
@bot.message_handler(commands=['start'])
def start(message):
    log.logger("Пользователь "+ message.from_user.first_name + " запустил бота",message.from_user.id, message.from_user.first_name, message.from_user.username)
    bot.send_message(message.chat.id, 'Привет, ' + message.from_user.first_name + ' Введи математическое выражение')
@bot.message_handler(func=lambda message: True)
def calc(message):
    try:
        x = message.text
        str = compile(x, 'string', 'eval')
        log.logger(x,message.from_user.id, message.from_user.first_name, message.from_user.username)
        c = eval(str)
        bot.send_message(message.chat.id, f"{message.text} = {c}")
        log.logger("Пользователь " + message.from_user.first_name + " получил ответ ",f"{message.text} = {c}", message.from_user.first_name, message.from_user.username)

    except ZeroDivisionError:
        bot.send_message(message.chat.id, 'На ноль делить нельзя')
        log.logger("Пользователь "+ message.from_user.first_name + " получил ответ:- 'На ноль делить нельзя'",message.from_user.id, message.from_user.first_name, message.from_user.username)

    except SyntaxError:
        bot.send_message(message.chat.id, 'Я понимаю только математические выражения')
        log.logger("Пользователь "+ message.from_user.first_name + " получил ответ:- 'Я понимаю только математические выражения'",message.from_user.id, message.from_user.first_name, message.from_user.username)

    except NameError:
        bot.send_message(message.chat.id, random.choice(seq=[("Я понимаю только математические выражения"), 
                                                             ("Если возникли сложности, отправьте боту /help"), 
                                                             ("Перефразируйте, "+ message.from_user.first_name + "!")]))
        log.logger("Пользователь "+ message.from_user.first_name + " получил ответ об ошибке",message.from_user.id, message.from_user.first_name, message.from_user.username)

bot.polling(none_stop=True)


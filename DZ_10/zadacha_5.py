"""С файлом зависимостей беда какая-то.
Никак не хочет добавлять пакеты установленные в окружении
Врчную в файл добавил пакет pyTelegramBotAPI без версии

На всякий  pip install pyTelegramBotAPI

"""


import telebot
import config
import logger as log
bot = telebot.TeleBot(config.CALC_BOT_TOKEN)


def get_coefficients_of_polynomial(poly: list) -> list:
    coefficients = []
    for i in poly:
        if ('x' in i) and ('(' in i):
            coefficients.append(
                [int(i[i.find('(')+1:i.find(')')]), int(i[0:i.find('*')])])
        elif ('x' in i) and ('(' not in i):
            coefficients.append([1, int(i[0:i.find('*')])])
        elif ('x' not in i) and (i != '+') and (i != '=') and (i != '0'):
            coefficients.append([0, int(i)])
    return coefficients

def pol(message):

    split_poly1 = poly1.split()
    split_poly2 = poly2.split()
    coef_list1 = get_coefficients_of_polynomial(split_poly1)
    coef_list2 = get_coefficients_of_polynomial(split_poly2)

    sum_str = str()

    for i in coef_list1:

        for j in coef_list2:
            if (j[0] == i[0] > 1):
                sum_str += f'{i[1]+j[1]}*x^({i[0]}) + '
            elif (j[0] == i[0] == 1):
                sum_str += f'{i[1]+j[1]}*x + '
            elif (j[0] == i[0] == 0):
                sum_str += f'{i[1]+j[1]} + '

    sum_str = sum_str[0:len(sum_str)-2]+'= 0'

    bot.send_message(message.chat.id, sum_str +' Для продолжения вычислений, снова запустите бот-  "/start"')
    log.logger(sum_str,message.from_user.id, message.from_user.first_name, message.from_user.username)



@bot.message_handler(commands=['start'])

def handle_text(message): 
    log.logger('Пользователь запустил бот',message.from_user.id, message.from_user.first_name, message.from_user.username)

    numvan1 = bot.send_message(message.chat.id, 'Я понимаю полиномы записанные ввиде- 74*x^(5) + 46*x^(4) + 188*x^(3) + 138*x^(2) + 20*x + 50 = 0')
    numvan = bot.send_message(message.chat.id, 'Введите 1 полином') 
    bot.register_next_step_handler(numvan ,num1_fun)

def num1_fun(message):
   global poly1
   poly1 = message.text
   log.logger(poly1,message.from_user.id, message.from_user.first_name, message.from_user.username)

   numtwo = bot.send_message(message.chat.id, 'ведите 2 число')
   bot.register_next_step_handler(numtwo ,num2_fun)
   
def num2_fun(message):
    global poly2
    poly2 = message.text 
    log.logger(poly2,message.from_user.id, message.from_user.first_name, message.from_user.username)
     
    operu = bot.send_message(message.chat.id, 'вычисляю' )
    
    pol(message)
    
bot.polling(none_stop=True)
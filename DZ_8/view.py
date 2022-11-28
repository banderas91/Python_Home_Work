import logger as log
def show_main_menu():
    while True:
        data = input('''Выберете действие:
        1 - Введите данные контакта
        2 - Записать данные контакта в базу данных
        3 - Отобразить содержимое БД
        4 - Удалить запись в БД по id контакта
        5 - Импортировать контаткы в базу из CSV
        6 - Экспортировать контакты из базы в CSV
        0 - Закончить работу
        ''')
        if data == '': break
        if not data in ['1', '2', '3', '4', '5', '6', '7','8','9','10','0']:
            print('Неправильный ввод. Введите еще раз!')
        else:
            return int(data)


        

def show_surname():
    while True:  
        surname = input("Введите фамилию ")  
        if len(surname)!=0:  
            log.logger("Пользователь ввел Фамилию", surname)
            return surname  
        else:
            log.logger("Пользователь ошибся при вводе фамилии",surname)

            print("Пожалуйста, введите фамилию")   
            


def show_name():
    while True: 
        name = input("Введите имя ")  
        if len(name)!=0:
            log.logger("Пользователь ввел имя", name)  
            return name  
        else:
            log.logger("Пользователь ошибся при вводе имени",name)  
            print("Пожалуйста, введите имя ") 


def show_telephone():
    while True:
        telephone = input("Введите телефон  ")  
        log.logger("Пользователь ввел телефон", telephone)
        return telephone
        
             


def show_description():
    while True:
        description = input('Введите описание: ')
        if len(description)!=0:
            log.logger("Пользователь ввел описание", description)  
            return description  
        else: 
            log.logger("Пользователь ошибся при вводе описания",description) 
            print("Пожалуйста, введите описание ")
        



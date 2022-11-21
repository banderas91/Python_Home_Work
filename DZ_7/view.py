def show_main_menu():
    while True:
        data = input('''Выберете действие:
        1 - добавить контакт
        2 - имнортировать контакты из csv-файла
        3 - вывести контакты в csv-файл
        4 - вывести контакты в xml-файл
        5 - вывести контакты в JSON-файл
        6 - закончить работу
        ''')
        if data == '': break
        if not data in ['1', '2', '3', '4', '5', '6']:
            print('Неправильный ввод. Введите еще раз!')
        else:
            return int(data)
    return None


def show_surname():
    while True:  
        surname = input("Введите фамилию ")  
        if len(surname)!=0:  
            return surname  
        else:  
            print("Пожалуйста, введите фамилию")   


def show_name():
    while True: 
        name = input("Введите имя ")  
        if len(name)!=0:  
            return name  
        else:  
            print("Пожалуйста, введите имя ") 


def show_telephone():
    while True:
        telephone = input("Введите телефон  ")  
        # if not telephone.isdigit():  
        return telephone
        # else:
        #     print("Вводите только цифры")  
             


def show_description():
    while True:
        description = input('Введите описание: ')
        if len(description)!=0:  
            return description  
        else:  
            print("Пожалуйста, введите описание ")
        


def show_filename():
    while True:
        filename = input('Введите имя файла ')
        if len(filename)!=0:  
            return filename  
        else:  
            print("Пожалуйста, имя файла ")
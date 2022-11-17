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
        surname = input('Введите фамилию: ')
        if surname == '': break
        else:
            return surname
    return None


def show_name():
    while True:
        name = input('Введите имя: ')
        if name == '':
            break
        else:
            return name
    return None


def show_telephone():
    while True:
        telephone = input('Введите телефон: ')
        if telephone == '':
            break
        else:
            return telephone
    return None


def show_description():
    while True:
        description = input('Введите описание: ')
        if description == '':
            break
        else:
            return description
    return None


def show_filename():
    while True:
        filename = input('Введите имя файла ')
        if filename == '':
            break
        else:
            return filename
    return None
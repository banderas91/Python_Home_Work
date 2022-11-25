import view
import model
import bd 
import sqlite3
from sqlite3 import Error
import logger as log

FILENAME_DATA = 'phonebook.txt'


def select_action():
    while True:
        data = view.show_main_menu()
        if not data or data == 0: break

        if data == 1:
            log.logger("Пользователь нажал 1 что бы добавить контакт", data)
            surname = view.show_surname()
            name = view.show_name()
            tel = view.show_telephone()
            description = view.show_description()
            entry = model.create_contact(surname, name, tel, description)
            model.add_contact(FILENAME_DATA, entry)

        
        if data == 2:
            log.logger("Пользователь нажал 2 для записи контакта в базу данных", data)
    
            def sql_connection():
            
                try:
            
                    con = sqlite3.connect('mydatabase.db')
            
                    return con
            
                except Error:
            
                    print(Error)
            
            def sql_table(con):
            
                cursorObj = con.cursor()
            
                cursorObj.execute("""CREATE TABLE if not exists employees (
                                                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                            surname TEXT,
                                                            name TEXT,
                                                            tel TEXT,
                                                            description TEXT
                                                        )""")
                con.commit()
            
            con = sql_connection()
            sql_table(con)

            

            def sql_insert(con, entities):

                con = sqlite3.connect('mydatabase.db')
            
                cursorObj = con.cursor()
            
                cursorObj.execute('INSERT INTO employees(surname, name, tel, description ) VALUES( ?, ?, ?, ?)', entities)

                con.commit()
            
            entities = ( surname, name, tel, description)
            
            sql_insert(con, entities)
            
        if data == 3:
            log.logger("Пользователь нажал 3 для отображения в консоле содержимого базы данных", data)

            con = sqlite3.connect('mydatabase.db')
            bd.sql_fetch(con)
            break

        if data == 4:
            log.logger("Пользователь нажал 4 для удаления строки из базы", data)
            
            uId= (input("Введите id сотрудника  "))
            log.logger("Пользователь выбрал для удаления сотрудника c id", uId) 
            bd.delete_sqlite_record(uId)
        
        if data == 5:
            log.logger("Пользователь нажал 5 для импортирования содержимого из CSV файла в БД  ", data)
            bd.import_csv()
            
        if data == 6:
            log.logger("Пользователь нажал 6 для экспорта содержимого базы данных в CSV файл", data)

            bd.export_csv()
    
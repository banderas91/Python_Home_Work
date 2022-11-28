
import sqlite3
import csv
import os
import logger as log

con = sqlite3.connect('mydatabase.db')


def sql_fetch(con):
    
    cursorObj = con.cursor()

    cursorObj.execute('SELECT * FROM employees')
 
    rows = cursorObj.fetchall()
 
    for row in rows:
 
        print(row)
        log.logger("Пользователю отобразилось содержимое БД", row)
 

def delete_sqlite_record(uId):

    connection_obj = sqlite3.connect('mydatabase.db')

    cursor_obj = connection_obj.cursor()

    cursor_obj.execute("DELETE FROM employees WHERE id = ?", (uId))

    connection_obj.commit()
    connection_obj.close()
    log.logger("Пользователь удалил строку с id", uId)

def import_csv():

    con = sqlite3.connect('mydatabase.db')

    cur = con.cursor()
    


    with open('import_to_bd.csv','r') as fin:
        dr = csv.DictReader(fin, delimiter=";")
        to_db = [(i['surname'], i['name'], i['tel'], i['description']) for i in dr]

    cur.executemany("INSERT INTO employees (surname, name, tel, description) VALUES (?, ?, ?, ?);", to_db)
    con.commit()
    con.close()



def export_csv():
    conn=sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    cursor.execute("select * from employees")
    with open("employees_data.csv", "w") as csv_file:

        csv_writer = csv.writer(csv_file, delimiter="\t")
        csv_writer.writerow([i[0] for i in cursor.description])
        csv_writer.writerows(cursor)

    dirpath = os.getcwd() + "/employees_data.csv"
    print ( "Data exported Successfully into {}".format(dirpath))


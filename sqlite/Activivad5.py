import sqlite3
from DataBaseManager import DataBaseManager

dataBaseManager = DataBaseManager()


con = sqlite3.connect(dataBaseManager.database)
materia = (4,'matematicas', 'jovany', 9)
if not dataBaseManager.is_an_existing_materia(con,materia):
    dataBaseManager.create_materias(con, materia)
cur = con.cursor()
cur.execute("select * from materias;")
table_list = cur.fetchall()
for row in table_list:
    print(row)
    con.close()
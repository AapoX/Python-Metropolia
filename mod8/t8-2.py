import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='lentokentat',
         user='root',
         password='password',
         autocommit=True
         )


def haeMaakoodi(maak):
    sql = "SELECT type, COUNT(type) FROM airport "
    sql += "WHERE iso_country = '" + maak + "' "
    sql += "GROUP BY type;"
    print(sql)
    kursori = connection.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0:
        for i in tulos:
            print(i)
    return

maak = input("Anna Maan koodi:  ")
haeMaakoodi(maak)

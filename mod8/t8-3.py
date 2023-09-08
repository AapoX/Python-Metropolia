import mysql.connector
from geopy.distance import geodesic

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='lentokentat',
    user='root',
    password='password',
    autocommit=True
)


def haeKoordinaatit(maak):
    sql = "SELECT latitude_deg, longitude_deg FROM airport"
    sql += " WHERE ident = '" + maak + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    cursor.close()
    return (result[0], result[1])

maak1 = input("Anna ICAO 1:")
koordinaatit1 = haeKoordinaatit(maak1)

maak2 = input("Anna ICAO 2:")
koordinaatit2 = haeKoordinaatit(maak2)

if koordinaatit1 and koordinaatit2:
    distance = geodesic(koordinaatit1, koordinaatit2).kilometers
    print(f"The distance between {maak1} and {maak2} is approximately {distance:.2f} kilometers.")
else:
    print("Invalid ICAO codes. Make sure the airports exist in the database.")

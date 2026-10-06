import psycopg2

def find_customers_from(city):
    query = """SELECT     klantnr, plaats, adres
               FROM       Klant
               WHERE      plaats = %s;"""

    with conn.cursor() as cursor:
        data = (city, )
        cursor.execute(query, data)
        records = cursor.fetchall()

    return records

connection_string = "host='localhost' port='5433' dbname='fabriek' user='postgres' password='wachtwoord123'"
conn = psycopg2.connect(connection_string)
customers = find_customers_from('Amersfoort')
conn.close()

for record in customers:
    print(record[0])

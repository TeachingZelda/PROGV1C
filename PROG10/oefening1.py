import psycopg2

connection_string = "host='localhost' port='5433' dbname='fabriek' user='postgres' password='wachtwoord123'"

conn = psycopg2.connect(connection_string)
cursor = conn.cursor()

query = """
SELECT klantnr, plaats, adres
FROM Klant
WHERE plaats = 'Amersfoort';
"""

cursor.execute(query)
records = cursor.fetchall()

conn.close()

for record in records:
    print(record[0])
import psycopg2

connection_string = "host='localhost' port='5433' dbname='fabriek' user='postgres' password='wachtwoord123'"

conn = psycopg2.connect(connection_string)
cursor = conn.cursor()

query = """INSERT INTO Fabriek (fabnr, naam, adres, plaats)
           VALUES (457, 'FietsenWonder', 'Wielenlaan 8', 'Eindhoven');"""


cursor.execute(query)

conn.commit()
conn.close()

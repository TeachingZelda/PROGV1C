import psycopg2

id = input("Unique id: ")
name = input("Name: ")
addr = input("Address: ")
city = input("City: ")

connection_string = "host='localhost' port='5433' dbname='fabriek' user='postgres' password='wachtwoord123'"

conn = psycopg2.connect(connection_string)
cursor = conn.cursor()

query = """INSERT INTO Fabriek (fabnr, naam, adres, plaats)
           VALUES (%s, %s, %s, %s);"""

data = (id, name, addr, city)
cursor.execute(query, data)

conn.commit()
conn.close()

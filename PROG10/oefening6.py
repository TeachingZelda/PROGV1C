import psycopg2
# Verbinding maken met de database
connection_string = """
host='localhost'
port='5433'
dbname='filmtracker'
user='postgres'
password='wachtwoord123'
"""

conn = psycopg2.connect(connection_string)
cursor = conn.cursor()


# Gegevens van de film vragen
titel = input("Welke film heb je gekeken? ")
genre = input("Welk genre? ")
cijfer = int(input("Welk cijfer geef je de film? "))


# Film toevoegen aan de database
query = """
INSERT INTO movie (titel, genre, cijfer)
VALUES (%s, %s, %s);
"""

cursor.execute(query, (titel, genre, cijfer))
conn.commit()

print("Film opgeslagen!")


# Alle films uit de database ophalen
query = """
SELECT titel, genre, cijfer
FROM movie;
"""

cursor.execute(query)
films = cursor.fetchall()

print("\n--- Mijn films ---")

for film in films:
    print(f"{film[0]} | {film[1]} | {film[2]}/10")


# Alleen films met een 8 of hoger ophalen
query = """
SELECT titel, genre, cijfer
FROM movie
WHERE cijfer >= 8;
"""

cursor.execute(query)
aanraders = cursor.fetchall()

print("\n--- Aanraders ---")

for film in aanraders:
    print(f"{film[0]} | {film[1]} | {film[2]}/10")


# Verbinding met de database sluiten
cursor.close()
conn.close()
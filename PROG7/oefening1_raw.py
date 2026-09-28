# 1. Definieer een dictionary ‘telefoonboek’ met jouw naam (key)
#   en telefoonnummer (value).
# 2. Voeg iemand toe.
# 3. Vraag nu de gebruiker om een naam + nummer,
#   en voeg deze ook toe aan de dictionary.
# 5. Print het telefoonboek uit, met een for-loop.
#   Print elke naam/nummer op een eigen regel!

telefoonboek = {"Zelda": "06112121212"}
telefoonboek["Dima"] = "067373737373"
naam = input("Wat is uw naam? ")
nummer = input("Wat is uw telefoonnummer? ")
telefoonboek[naam] = nummer
print(telefoonboek)
for naam in telefoonboek:
    print(naam, "=", nummer)

telefoonboek = { "Zelda": "061234567"}

telefoonboek["Sam"] = "0678901234"

naam = input("Wat is je naam? ")
nummer = input("Wat is je nummer? ")

telefoonboek[naam] = nummer

for key, value in telefoonboek.items():
    print(key, value)

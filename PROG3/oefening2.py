# 1. Vraag de gebruiker het woord 'Python' in te voeren.
#       Print of de ingevoerde tekst wel of niet correct is.

tekst = input("Type het woord Python")
if tekst == "Python":
    print("Goed zo!")
else:
    print("Dat is niet correct!")

leeftijd = input("Wat is je leeftijd?")
if int(leeftijd) <= 18:
    print("Je mag stemmen")
else:
    print("Je mag niet stemmen")

gebruikersnaam = "DolleHond"
wachtwoord = "123Wachtwoord"

in_gebruikersnaam = input("Wat is je gebruikersnaam?")
in_wachtwoord = input("Wat is je wachtwoord?")

if in_gebruikersnaam == gebruikersnaam and in_wachtwoord == wachtwoord:
    print("Je bent ingelogd!")
else:
    print("Gebruikersnaam of wachtwoord is incorrect!")


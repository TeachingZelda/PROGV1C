leeftijd = input("Wat is je leeftijd?")
paspoort = input("Heb je een nederlands paspoort?")

if int(leeftijd) >= 18 and paspoort == "ja":
    print("Gefeliciteerd, je mag stemmen")
else:
    print("Je mag niet stemmen")
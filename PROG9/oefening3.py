while True:
    try:
        uurloon = float(input("Wat verdien je per uur: "))
        uren = int(input("Hoeveel uur heb je gewerkt: "))
        salaris = uurloon * uren
        print(f"{uren} uur werken levert €{salaris} op")
        break
    except:
        print("Ongeldige invoer. Probeer het opnieuw.")
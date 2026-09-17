#Schrijf (en test) een functie new_password() die 2 parameters
    # heeft: oldpassword en newpassword.
    # De return-waarde is True als het nieuwe password voldoet aan
    # de eisen.
    # Het nieuwe password wordt alleen geaccepteerd als het verschilt
    # van het oude password èn als het minimaal 6 tekens lang is.
    # Als dat niet zo is, is de return-waarde False.

def new_password(oldpassword, newpassword):
    if newpassword == oldpassword and len(newpassword) < 6:
        return False
    return True

old = input("Wat is je oude wachtwoord? ")
new = input("Wat is je nieuwe wachtwoord? ")

gelukt = new_password(old, new)
print(gelukt)

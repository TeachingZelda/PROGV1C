lijst = []
for i in range(0,5):

    invoer=input("Geef een getal: ")
    if int(invoer) == 0:
        break
    else:
        lijst.append(int(invoer))

print(sum(lijst))
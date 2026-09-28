fruitmand = {"appel":3, "banaan":5, "kers":50}

# print(fruitmand.keys())
# print("Aantal fruitsoorten: ", len(fruitmand.keys()))
# print(fruitmand.values())
# print("Aantal vruchten: ", sum(fruitmand.values()))
#
# print(fruitmand.items())
# print("Voldoende voorraad van:")
# for x, y in fruitmand.items():
#     print(x, y)
#
fruitmand = {"appel": 3, "banaan": 5}
appel = fruitmand.get("appel", "ik heb niets")
mangos = fruitmand.get("mangos", 10)
print(mangos)


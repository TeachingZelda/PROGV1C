fruitmand = {"appel": 3, "banaan": 5, "kers": 50}
print(fruitmand)
fruitmand.pop("appel")
print(fruitmand)
verwijderd = fruitmand.pop("banaan")
print(fruitmand)
del fruitmand["kers"]
print(fruitmand)

# print("\n", verwijderd)

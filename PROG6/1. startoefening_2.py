personen = [(naam.upper(), int(leeftijd)) for naam, leeftijd in (r.strip().split(",") for r in open("huisgenoten.txt"))]

for naam, leeftijd in personen:
    print(f"{naam}: {'Baby' if leeftijd < 1 else 'Kind' if leeftijd < 18 else 'Volwassen'}")

print(f"Het aantal huisgenoten is {len(personen)}\nDe som van de leeftijden is {sum(l for _, l in personen)}")
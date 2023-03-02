def lbs_to_kg(pounds):
    return pounds * 0.45359237

lbs = float(input("Geben Sie das Gewicht in Pfund ein: "))
kg = lbs_to_kg(lbs)

print("{0} Pfund sind {1:.2f} Kilogramm".format(lbs, kg))

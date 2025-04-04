x = int(input("Deine Erste Zahl zum addieren ist:"))
y = int(input("Jetzt brauche ich noch eine zweite Zahl:"))
request1 = input("Willst du noch eine weitere Zahl addieren?")

while True:
    if request1 == "ja" or "jo":
        z = int(input("Dann gib mir noch die Zusatzzahl:"))
        ergebnis1 = x + y + z
        print(f"Dann ist dein Ergebnis {ergebnis1}")
    else:
        ergebnis2 = x + y
        print(f"Dann ist dein Ergebnis {ergebnis2}")

decimal_num = int(input("Enter a decimal number: "))

def decimal_to_binary(decimal_num):
    binary_num = []
    while decimal_num > 0:
        binary_num.append(decimal_num % 2)
        decimal_num = decimal_num // 2
    binary_num.reverse()
    return binary_num

binary_representation = decimal_to_binary(decimal_num)
print(f"The binary representation of {decimal_num} is: {binary_representation}")



'''Die Funktion decimal_to_binary nimmt eine Dezimalzahl decimal_num als Eingabe.
Sie initialisiert eine leere Liste binary_num, um die binäre Darstellung der Dezimalzahl zu speichern.
Die while-Schleife läuft solange, wie decimal_num größer als 0 ist.
In jeder Iteration der while-Schleife wird der Rest bei der Division von decimal_num durch 2 mithilfe der append-Methode zur Liste binary_num hinzugefügt. Dieser Rest stellt das nächste Binärziffer in der Binärdarstellung der Dezimalzahl dar.
Der Wert von decimal_num wird aktualisiert, indem er durch 2 ganzzahlig geteilt wird (decimal_num = decimal_num // 2).
Nach Beendigung der while-Schleife wird die Reihenfolge von binary_num mit der reverse-Methode umgekehrt.
Die Funktion gibt die umgekehrte Liste binary_num zurück, die die Binärdarstellung der Dezimalzahl enthält.'''

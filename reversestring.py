def reverse_string(string):
    # Kehrt die Reihenfolge der Zeichen in einem String um.
    reversed_string = string[::-1]
    return reversed_string



# Test der Funktion
original_string = input("Enter Your String that you Want to Reverse: ")
reversed_string = reverse_string(original_string)
print(reversed_string)

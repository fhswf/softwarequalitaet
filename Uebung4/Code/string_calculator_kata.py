# TODO: Implementiere den String Calculator mit TDD
# Hinweise: Beginne mit den Basisregeln ("" -> 0, "1" -> 1, "1,2" -> 3)
# Erweitere schrittweise mit Tests für \n, benutzerdefinierte Delimiter, etc.

def add(numbers: str) -> int:
    string = numbers.replace("\n",",")
    string = string.split(",")
    result = 0
    if numbers:
        for number in string:
            if number.lstrip("-").isdigit():
                result+=int(number)
    return result
    pass
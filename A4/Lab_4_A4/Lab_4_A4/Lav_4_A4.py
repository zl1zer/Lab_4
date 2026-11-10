def isValidNumber(string):
    return string.isdigit() and len(string) in [13, 15, 16]


def getCheckSum(string):
    checkSum = 0

    for i in range(len(string) - 1, -1, -1):
        digit = int(string[i])

        if (len(string) - 1 - i) % 2 == 1:
            digit = digit * 2

            if digit > 9:
                digit = digit - 9

        checkSum = checkSum + digit

    return checkSum


def getCardType(string):
    if (len(string) == 13 or len(string) == 16) and string.startswith("4"):
        return "Visa"

    if len(string) == 15 and (string.startswith("34") or string.startswith("37")):
        return "American Express"

    if len(string) == 16 and string[:2] in ["51", "52", "53", "54", "55"]:
        return "Master Card"

    return "Invalid"



card_number = input("Введите номер карты: ")

if not isValidNumber(card_number):
    print("Неверный формат номера карты!")

elif getCheckSum(card_number) % 10 != 0:
    print("Номер карты не прошёл проверку Луна!")

else:
    card_type = getCardType(card_number)

    if card_type == "Invalid":
        print("Тип карты не определён!")
    else:
        print("Номер карты корректный!")
        print("Тип карты:", card_type)

def convert_letter_to_num(letter):
    switcher = {
        "A": 0,
        "B": 1,
        "C": 2,
        "D": 3,
        "E": 4,
        "F": 5,
        "G": 6,
        "H": 7,
        "I": 8,
        "J": 9,
        "K": 10,
        "L": 11,
        "M": 12,
        "N": 13,
        "O": 14,
        "P": 15,
        "Q": 16,
        "R": 17,
        "S": 18,
        "T": 19,
        "U": 20,
        "V": 21,
        "W": 22,
        "X": 23,
        "Y": 24,
        "Z": 25
    }
    return switcher.get(letter, 26)


while True:
    phrase = input("Enter a phrase: ").upper().split()

    finalNums = ""

    for word in phrase:
        letters = [x for x in word]
        letters.reverse()

        num = 0
        i = 0
        for l in letters:
            num = num + (convert_letter_to_num(l) * (26 ** i))
            i += 1

        finalNums = finalNums + str(num) + " "

    print(finalNums)

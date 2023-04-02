from collections import OrderedDict

loop = True;

while loop:
    alphabet = [chr(number) for number in range(65,91)]

    plainText = input("<._.> Input the text: ").upper().replace("J","I")
    while not all(letter in alphabet for letter in plainText) or len(plainText) == 0:
        plainText = input("<-_-> Error! You can only enter letters. Try again: ").upper()

    if len(plainText) % 2 == 1: plainText += 'Z'
    pairs = [plainText[i:i+2] for i in range(0, len(plainText), 2)]

    key = input("<._.> Input the key: ").upper()
    while not all(letter in alphabet for letter in key):
        key = input("<-_-> Error! You can only enter letters. Try again: ").upper()

    alphabet.remove('J')
    keyList = list(OrderedDict.fromkeys([letter for letter in key] + alphabet))
    matrix = [keyList[i:i+5] for i in range(0, len(keyList), 5)]

    def findingCoordinates(letter):
        for row in range(5):
            for column in range(5):
                if letter == matrix[row][column]: 
                    return row, column

    encryptedText = str()

    for pair in pairs:
        y1, x1 = findingCoordinates(pair[0])
        y2, x2 = findingCoordinates(pair[1])
        if x1 == x2: 
            if y1 + 1 < 5: encryptedText += matrix[y1+1][x1]
            else: encryptedText += matrix[0][x1]
            if y2 + 1 < 5: encryptedText += matrix[y2+1][x2]
            else: encryptedText += matrix[0][x2]
        elif y1 == y2: 
            if x1 + 1 < 5: encryptedText += matrix[y1][x1+1]
            else: encryptedText += matrix[y1][0]
            if x2 + 1 < 5: encryptedText += matrix[y2][x2+1]
            else: encryptedText += matrix[y2][0]
        else:
            dif = x1 - x2
            encryptedText += matrix[y1][x1-dif]
            encryptedText += matrix[y2][x2+dif]

    print("<.w.>", encryptedText)
    
    loop = None;
    while loop == None:
        loop = input("<o.o> Do you want to encrypt again? Yes/No\n")
        if loop.upper() == "YES": loop = True;
        elif loop.upper() == "NO": loop = False;
        else: loop = None;

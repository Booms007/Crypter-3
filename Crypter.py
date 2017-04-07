# Javier Velazco
# Florida International University

import time

def methodASCII(sentence):
    start = time.clock()
    print('Starting ASCII Method...')
    fullString = ''
    for iterator in sentence:
        convertToASCII = ord(iterator)
        if (convertToASCII >= ord('a')) and (convertToASCII <= ord('z')):
            convertedLetter = ord('z') - convertToASCII + ord('a')
            convertToChar = chr(convertedLetter)
            fullString += str(convertToChar)
        else:
            fullString += str(chr(convertToASCII))
    end = time.clock()
    print("Converted message: " + fullString)
    print('Time taken: ' + str(round((end * 1000) - (start * 1000), 3)) + " seconds.")

def methodIf(sentence):
    start = time.clock()
    print('Starting If Staement Method...')
    fullString = ''
    for x in sentence:
        if x == 'a':
            fullString += str('z')
        elif x == 'b':
            fullString += str('y')
        elif x == 'c':
            fullString += str('x')
        elif x == 'd':
            fullString += str('w')
        elif x == 'e':
            fullString += str('v')
        elif x == 'f':
            fullString += str('u')
        elif x == 'g':
            fullString += str('t')
        elif x == 'h':
            fullString += str('s')
        elif x == 'i':
            fullString += str('r')
        elif x == 'j':
            fullString += str('q')
        elif x == 'k':
            fullString += str('p')
        elif x == 'l':
            fullString += str('o')
        elif x == 'm':
            fullString += str('n')
        elif x == 'n':
            fullString += str('m')
        elif x == 'o':
            fullString += str('l')
        elif x == 'p':
            fullString += str('k')
        elif x == 'q':
            fullString += str('j')
        elif x == 'r':
            fullString += str('i')
        elif x == 's':
            fullString += str('h')
        elif x == 't':
            fullString += str('g')
        elif x == 'u':
            fullString += str('f')
        elif x == 'v':
            fullString += str('e')
        elif x == 'w':
            fullString += str('d')
        elif x == 'x':
            fullString += str('c')
        elif x == 'y':
            fullString += str('b')
        elif x == 'z':
            fullString += str('a')
        else:
            fullString += str(x)
    end = time.clock()
    print("Converted message: " + fullString)
    print('Time taken: ' + str(round((end * 1000) - (start * 1000), 3)) + " seconds.")

print("Which method of encryption/decryption would you like to use: "
      + "\n(1) = ASCII Conversion" + '\n(2) = If Statement Conversion'
      + "\n(3) = Both" + "\n(Q) = Quit")

method = input()
method = method.lower()
while 1:
    if method == '1':
        print("Enter message to encrypt or decrypt: \n")
        message = input()
        methodASCII(message)
        break
    elif method == '2':
        print("Enter message to encrypt or decrypt: \n")
        message = input()
        methodIf(message)
        break
    elif method == '3':
        print("Enter message to encrypt or decrypt: \n")
        message = input()
        methodASCII(message)
        print('\n')
        methodIf(message)
        break
    elif method == 'q':
        break
    else:
        print('Incorrect option selected, try again')
        method = input()






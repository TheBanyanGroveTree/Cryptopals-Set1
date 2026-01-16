"""
Description: Determine which 60-char string in the .txt has been encrypted
by single-char XOR.
Author: Aahana Sapra
Date: 1/16/25
"""

import requests

# open url to .txt file
txtURL = "https://cryptopals.com/static/challenge-data/4.txt"
txtArr = requests.get(txtURL).text.splitlines()
"""
for line in txtArr:
    print(type(line))
    print(line)
"""

# initialize bytes object containing every char in ASCII table
asciiTable = bytes(range(128))

# define constants for scoring
SPACE = 10
LOWERCASE = 8
PUNCTUATION = 6
UPPERCASE = 4
WHITESPACE = 2

# define hex to bytes conversion function
def hexToBytes(hexStr):
    return bytes.fromhex(hexStr)

# define bytes to ASCII conversion function
def bytesToASCII(bytesArr):
    return bytesArr.decode('ascii')

# define xor function
def xorBytes(bytesArr1, bytesArr2):
    return bytes(a ^ b for a, b in zip(bytesArr1, bytesAr2))

# define character frequency counting function
def charFrequency(xorArr):
    frequency = {}
    for elemeny in xorArr:
        # set count to 0 if key doesn't exist
        frequency[element] = frequency.get(element, 0) + 1

    return frequency

# define function to calculate score of current ASCII key
def calculateScore(frequency):
    score = 0
    for key in frequency:
        # space char
        if (key == 32):
            score += SPACE
        # lowercase letter
        elif (97 <= key <= 122):
            score += LOWERCASE
        # puncutation
        elif (key in [33, 34, 39, 44, 45, 46, 58, 59, 63]):
            score += PUNCTUATION
        # uppercase letter
        elif (65 <= key <= 90):
            score += UPPERCASE
        # whitespace characters
        elif (9 <= key <= 13):
            score += WHITESPACE

    return score

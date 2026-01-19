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
    return bytes(a ^ b for a, b in zip(bytesArr1, bytesArr2))

# define character frequency counting function
def charFrequency(xorArr):
    frequency = {}
    for element in xorArr:
        # set count to 0 if key doesn't exist
        frequency[element] = frequency.get(element, 0) + 1

    return frequency

# define function to calculate score of current ASCII key
def calculateScore(frequency):
    score = 0
    for key, count in frequency.items():
        # space char
        if (key == 32):
            score += (SPACE * count)
        # lowercase letter
        elif (97 <= key <= 122):
            score += (LOWERCASE * count)
        # puncutation
        elif (key in [33, 34, 39, 44, 45, 46, 58, 59, 63]):
            score += (PUNCTUATION * count)
        # uppercase letter
        elif (65 <= key <= 90):
            score += (UPPERCASE * count)
        # whitespace characters
        elif (9 <= key <= 13):
            score += (WHITESPACE * count)

    return score

# define function to determine best key
def topScoreAndKey(hexStr):
    scoreArr = [0] * 128
    # xor hex encoded string against every possible ASCII char
    for i in range(len(asciiTable)):
        currentCharArr = bytearray([i] * len(hexToBytes(hexStr)))
        currentXOR = xorBytes(currentCharArr, hexToBytes(hexStr))
        currentFrequency = charFrequency(currentXOR)

        # calculate score for each ASCII char and add to score array
        scoreArr[i] = calculateScore(currentFrequency)

    # determine key corresponding to top score
    topScore = 0;
    topIndex = 0;
    for i in range(len(scoreArr)):
        if (scoreArr[i] > topScore):
            topScore = scoreArr[i]
            topIndex = i
    
    # return top score and index for corresponding key
    return (topScore, topIndex)

# define function to determine encrypted 60-char string
def topXORStr():
    topScore = 0
    bestKey = 0
    topLine = ""

    for line in txtArr:
        score, key = topScoreAndKey(line)
        if (score > topScore):
            topScore = score
            bestKey = key
            topLine = line

    decodedStr = xorBytes(bytearray([bestKey] * len(hexToBytes(topLine))),
                      hexToBytes(topLine))

    # comma adds a space in between elements
    print("Key:", chr(bestKey))
    print("Decoded:", bytesToASCII(decodedStr))

topXORStr()

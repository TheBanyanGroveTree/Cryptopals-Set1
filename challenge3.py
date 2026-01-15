"""
Description: Find the key for a single-byte XOR cipher
Author: Aahana Sapra
Date: 1/15/2026
"""

# initialize hex string
hexStr = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

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

# def bytes to ASCII conversion function
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
    for key in frequency:
        # space char
        if(key == 32):
            score += SPACE
        # lowercase letter
        elif (97 <= key <= 122):
            score += LOWERCASE
        # punctuation
        elif (key in [33, 34, 39, 44, 45, 46, 58, 59, 63]):
            score += PUNCTUATION
        # uppercase letter
        elif (65 <= key <= 90):
            score += UPPERCASE
        # whitespace characters
        elif (9 <= key <= 13):
            score += WHITESPACE

    return score

# define function to determine best key
def topScore():
    scoreArr = [0] * 128
    # xor hex encoded string against every possible ASCII char
    for i in range(len(asciiTable)):
        currentCharArr = bytearray([i] * 128)
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
    
    # output key and decoded string
    print("Key: " + chr(topIndex))
    topXOR = xorBytes(bytearray([topIndex] * 128), hexToBytes(hexStr))
    print("Decoded: " + str(bytesToASCII(topXOR)))
                
# test progress
topScore()

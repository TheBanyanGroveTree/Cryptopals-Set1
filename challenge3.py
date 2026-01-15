"""
Description: Find the key for a single-byte XOR cipher
Author: Aahana Sapra
Date: 1/14/2026
"""

# initialize hex string
hexStr = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

# initialize bytes object containing every char in ASCII table
asciiTable = bytes(range(128))

# define constants for scoring
LOWERCASE = 2
UPPERCASE = 1
SYMBOLS_AND_WHITESPACE = 1

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
        # lowercase letters
        if ((frequency[key] >= 97) and (frequency[key] <= 122)):
            score += LOWERCASE
        # uppercase letters
        elif (65 <= frequency[key] <= 90):
            score += UPPERCASE
        # symbols, numbers, and whitespace characters
        elif ((9 <= frequency[key] <= 13) or
              (32 <= frequency[key] <= 64) or
              (91 <= frequency[key] <= 96) or
              (123 <= frequency[key] <= 126)):
            score += SYMBOLS_AND_WHITESPACE

    return score

# define function to determine best key
def topScore():
    scoreArr = [0] * 128
    # xor hex encoded string against every possible ASCII char
    for i in range(len(asciiTable)):
        currentCharArr = bytearray([i] * 128)
        xor = xorBytes(currentCharArr, hexToBytes(hexStr))
        frequency = charFrequency(xor)
        print(frequency)

        # calculate score for each ASCII char and add to score array
        scoreArr[i] = calculateScore(frequency)

    # determine top score
    
                
# test progress
topScore()

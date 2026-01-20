"""
Description: Break repeating-key XOR
Author: Aahana Sapra 
Date: 1/18/25
"""

import requests
import base64

# open url to .txt file and read contents
txtURL = "https://cryptopals.com/static/challenge-data/6.txt"
txtArr = requests.get(txtURL).text.splitlines()
"""
for line in txtArr:
    print(type(line))
    print(line)
"""

# initialize constants for min and max key size
MIN_KEY_SIZE = 2
MAX_KEY_SIZE = 40

# initialize bytes object containing every char in ASCII table
asciiTable = bytes(range(128))

# define constants for scoring
SPACE = 10
LOWERCASE = 8
PUNCTUATION = 6
UPPERCASE = 4
WHITESPACE = 2

# define base64 to bytes conversion function
def base64ToBytes(base64Str):
    return base64.b64decode(base64Str)

# define xor function
def xorBytes(bytesArr1, bytesArr2):
    return bytes(a ^ b for a, b in zip(bytesArr1, bytesArr2))

# define function to calculate hamming distance
def hammingDistance(xor):
    return int.from_bytes(xor, byteorder='big').bit_count()

"""
# Test hamming distance calculation
# define ASCII to bytes conversion function
def asciiToBytes(asciiStr):
    return asciiStr.encode('ascii')

str1 = asciiToBytes("this is a test")
str2 = asciiToBytes("wokka wokka!!!")
testXOR = xorBytes(str1, str2)
print(hammingDistance(testXOR))
"""

# define function to calculate normalized hamming distance
def normalizedHammingDistance(data, keySize):
    # not enough data to compare
    if (len(data) < (2 * keySize)):
        return 0.0

    # initialize var to calculate average
    totalHamDist = 0
    numComparisons = 0
    
    # compare blocks of length keySize
    for i in range(0, (len(data) - (2 * keySize) + 1), keySize):
        # extract chucks of length keySize
        block1 = data[i : (i+keySize)]
        block2 = data[(i+keySize) : (i + (2 * keySize))]

        # calculate hamming distance between blocks
        blockHamDist = hammingDistance(xorBytes(block1, block2))

        # update values for calculating average
        totalHamDist += blockHamDist
        numComparisons += 1

    # calculate normalized hamming distance
    if (numComparisons == 0):
        return 0.0

    averageHamDist = totalHamDist / numComparisons
    normalizedHamDist = averageHamDist / keySize

    return normalizedHamDist

# define function to determine key size with smallest normalized hamming dist
def determineKeySize(data):
    normDistDict = {}
    for key in range(MIN_KEY_SIZE, MAX_KEY_SIZE):
        normDistDict[key] = normalizedHammingDistance(data, key)

    # compare elements based on value (second item in tuple)
    smallestPair = min(normDistDict.items(), key=lambda item: item[1])

    return smallestPair[0] # return key size

# define function to split ciphertext into blocks of length key size
def splitBlocks(data, keySize):
    return [data[i:i+keySize] for i in range(0, len(data), keySize)]

# define function to transpose blocks
def transpose(data, keySize):
    blocks = splitBlocks(data, keySize)
    # * = unpacking operator
    # zip() extracts elements from iterables based on index
    transposedBlocks = list(zip(*blocks))
    return transposedBlocks

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

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

# define base64 to bytes conversion function
def base64ToBytes(base64Str):
    return base64.b64decode(base64Str)

# define xor function
def xorBytes(bytesArr1, bytesArr2):
    return bytes(a ^ b for a, b in zip(bytesArr1, bytesArr2))

# define function to calculate hamming distance
def hammingDistance(xor):
    return xor.bit_count()

# define function to calculate normalized hamming distance
def normalizedHammingDistance(xor, keySize):
    # not enough data to compare
    if (len(xor) < (2 * keySize)):
        return 0.0

    # initialize var to calculate average
    totalHamDist = 0
    numComparisons = 0
    
    # compare blocks of length keySize
    for i in range(0, len(xor) - xor, xor):
        # extract chucks of length keySize
        block1 = xor[i : (i+keySize)]
        block2 = xor[(i+keySize) : (i + (2 * keySize))]

        # calculate hamming distance between blocks
        blockHamDist = hammingDistance(xorBytes(block1, block2))

        # update values for calculating average
        totalHamDist += blockHamDist
        numComparisons += 1

    # calculate normalized hamming distance
    averageHamDist = totalHamDist / numComparisons
    normalizedHamDist = averageHamDist / keySize

    return normalizedHamDist

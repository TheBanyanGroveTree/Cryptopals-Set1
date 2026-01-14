"""
Description: Find the key for a single-byte XOR cipher
Author: Aahana Sapra
Date: 1/14/2026
"""

# initialize hex string
hexStr = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

# initialize bytes object containing every char in ASCII table
asciiTable = bytes(range(128))

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

# define score function
def score():
    # xor hex encoded string against every possible ASCII char
    for i in range(len(asciiTable)):
        currentCharArr = bytearray([i] * 128)
        xor = bytesToASCII(xorBytes(currentCharArr, hexToBytes(hexStr)))
        frequency = charFrequency(xor)
        print(frequency)
        
# test progress
score()

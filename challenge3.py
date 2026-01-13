"""
Description: Find the key for a single-byte XOR cipher
Author: Aahana Sapra
Date: 1/8/2026
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



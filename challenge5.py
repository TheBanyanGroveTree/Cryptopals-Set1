"""
Description: Implement repeating-key XOR in Python
Author: Aahana Sapra
Date: 1/18/25
"""

# define ASCII to bytes conversion function
def asciiToBytes(asciiStr):
    return asciiStr.encode('ascii')

# define bytes to hex conversion function
def bytesToHex(bytesArr):
    return bytesArr.hex()

# define repeated key XOR function
def repeatedKeyXOR(plaintext, key):
    keyLen = len(key)
    encoded = []

    for i in range(len(plaintext)):
        encoded.append(plaintext[i] ^ key[i % keyLen])

    return bytes(encoded)

# convert strings to bytes
plaintext = asciiToBytes("Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal")
key = asciiToBytes("ICE")

# output results
print(bytesToHex(repeatedKeyXOR(plaintext, key)))

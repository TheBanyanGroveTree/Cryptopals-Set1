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
        print("plaintext data type:", type(plaintext[i]))
        print("key data type:", type(key[i % keyLen]))
        encoded.append(plaintext[i] ^ key[i % keyLen])

    return bytes(encoded)

# convert strings to bytes
plaintext = asciiToBytes("Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal")
print(type(plaintext))
key = asciiToBytes("ICE")
print(type(key))

# output results
print(bytesToHex(repeatedKeyXOR(plaintext, key)))

"""
Description: This program performs the XOR of 2 buffers.
Author: Aahana Sapra
Date: 1/8/2026
"""

# define hex to bytes conversion function
def hexToBytes(hexStr):
    return bytes.fromhex(hexStr)

# define xor function
def xorBytes(bytesArr1, bytesArr2):
    return bytes(a ^ b for a, b in zip(bytesArr1, bytesArr2))

# define bytes to hex conversion function
def bytesToHex(bytesArr):
    return bytesArr.hex()

# initialize hex strings
buffer1 = "1c0111001f010100061a024b53535009181c"
buffer2 = "686974207468652062756c6c277320657965"

# call functions
bytesArr1 = hexToBytes(buffer1)
bytesArr2 = hexToBytes(buffer2)
xor = xorBytes(bytesArr1, bytesArr2)
print(bytesToHex(xor))

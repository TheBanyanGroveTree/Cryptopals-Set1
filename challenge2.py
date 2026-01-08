"""
Description: This program performs the XOR of 2 buffers.
Author: Aahana Sapra
Date: 1/8/2026
"""

# initialize hex string
buffer1 = "1c0111001f010100061a024b53535009181c"
buffer2 = "686974207468652062756c6c277320657965"

# define hex to bytes conversion function
def hexToBytes(hexString):
    byteArray = bytes.fromhex(hexString)
    return byteArray

# define xor function
def xorBytes(byteArr1, byteArr2):
    xor = bytes(a ^ b for a, b in zip(byteArr1, byteArr2))
    return xor

# define bytes to hex conversion function
def bytesToHex(byteArray):
    hexString = byteArray.hex()
    return hexString

# call functions
byteArr1 = hexToBytes(buffer1)
byteArr2 = hexToBytes(buffer2)
xor = xorBytes(byteArr1, byteArr2)
print(bytesToHex(xor))

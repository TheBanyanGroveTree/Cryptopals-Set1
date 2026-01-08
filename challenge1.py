"""
Description: This program implements functions that convert data encoded
in hex or base64 to bytes and vice versa.
Author: Aahana Sapra
Date: 1/8/2026
"""

import base64

# define hex to bytes conversion function
def hexToBytes(hexStr):
    return bytes.fromhex(hexStr)

# define base64 to bytes conversion function
def base64ToBytes(base64Str):
    return base64.b64decode(base64Str)

# define bytes to hex conversion function
def bytesToHex(bytesArr):
    return bytesArr.hex()

# define bytes to base64 conversion function
def bytesToBase64(bytesArr):
    return base64.b64encode(bytesArr)

# initialize hex string
hexStr = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

# call functions
bytesArr = hexToBytes(hexStr)
print(bytesToBase64(bytesArr).decode('utf-8'))

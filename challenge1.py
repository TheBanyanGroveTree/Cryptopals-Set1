"""
Description: This program implements functions that convert data encoded
in hex and base64 to bytes and vice versa.
Author: Aahana Sapra
Date: 1/8/2026
"""

import base64

# initialize hex and base64 strings
hexString = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

base64String = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

# define hex to bytes conversion function
def hexToBytes(hexString):
    byteArray = bytes.fromhex(hexString)
    return byteArray

# define base64 to bytes conversion function
def base64ToBytes(base64String):
    byteArray = base64.b64decode(base64String)
    return byteArray

# define bytes to hex conversion function
def bytesToHex(byteArray):
    hexString = byteArray.hex()
    return hexString

# define bytes to base64 conversion function
def bytesToBase64(byteArray):
    base64String = base64.b64encode(byteArray)
    return base64String

# call functions
print(bytesToBase64(hexToBytes(hexString)).decode('utf-8'))

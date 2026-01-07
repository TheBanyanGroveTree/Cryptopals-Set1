"""
Description:
Author: Aahana Sapra
Date: 1/7/2026
"""

import base64

hexString = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

base64String = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

def hexToBytes(hexString):
    byteArray = bytes.fromhex(hexString)
    return byteArray


def base64ToBytes(base64String):
    byteArray = base64.b64decode(base64String)
    return byteArray

def bytesToHex(byteArray):
    hexString = byteArray.hex()
    return hexString

def bytesToBase64(byteArray):
    base64String = base64.base64encode(byteArray)
    return base64String
    

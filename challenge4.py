"""
Description: Determine which 60-char string in the .txt has been encrypted
by single-char XOR.
Author: Aahana Sapra
Date: 1/16/25
"""

import requests

# open url to .txt file
txtURL = "https://cryptopals.com/static/challenge-data/4.txt"
txtArr = requests.get(txtURL).text.splitlines()
for line in txtArr:
    print(type(line))
    print(line)

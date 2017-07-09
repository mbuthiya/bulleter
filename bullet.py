#! usr/bin/python3.6
# A simple program that takes the items from the clipboard and adds a star infron of every new line and return it to the clipboard

import pyperclip

text = pyperclip.paste()

lines = text.split("\n")

for i in range(len(lines)):
    lines[i] = '* '+lines[i]

text = "\n".join(lines)

pyperclip.copy(text)

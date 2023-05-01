# README.md

## General information
All inputs are expected to be followed by a newline.
`num1` and `num2` must be positive integers. `num1` must be greater than or equal to `num2`. Not following this will cause
The binary should be run in the given virtual machine as a non root user only. Ensure the username contains only alphanumeric characters.

## Running
### To run in secured mode:
Run the binary (`./binary`)
1. First input `S` followed by a newline.
2. Then input the password followed by a newline.
3. Then input the first number followed by a newline.
4. Then input the second number followed by a newline.
5. The result of the computation will be printed.

If the incorrect password is entered, the binary will print an error message and then run the `add` function.

### To run in non-secured mode:

Run the binary.
1. First input `A` followed by a newline.
2. Then input the first number followed by a newline.
3. Then input the second number followed by a newline.
4. The result of the computation will be printed.
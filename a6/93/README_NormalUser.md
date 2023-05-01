# README for "FUNCTION HIDING"
## _USER = NORMAL_USER_

To run the binary use:
```sh
chmod +x binary
./binary <FUNCTION_MODE> <INPUT-1> <INPUT-2> (optional)<PASSWORD>
```
where the arguments should be:

| ARGUMENT NUMBER | ARGUMENT NAME | ARGUMENT EXPLAINATION |  ARGUMENT EXAMPLE |
| ------ | ------ | ------ | ------ | 
| 0 | BINARY_NAME | Enter the name of the binary with "./" in the starting | ./binary | 
| 1 | FUNCTION_MODE | Enter '1' (Hidden Function) OR '2' (Sum Function) | 2 | 
| 2 | INPUT-1 | Enter the value of the first number to be passed to the selected function | 8 | 
| 3 | INPUT-2 | Enter the value of the second number to be passed to the selected function | 5 | 
| 4 (Optional) | PASSWORD | Enter password. This is optional, and is required only incase if you want to run the hidden function | DummYpAssWoRD | 

### SUPERUSER Authentiaction:

The `superuser` is given a specific PASSWORD, on entering which as the `4th` optional argument while running the given binary, the binary gets 'superuser' privileges & will be able to run the hidden function.

> `SHA512` hash of the enetered password is computed & checked against a precalculated hash value inorder to authenticate the superuser. 
> If the computed hash value & the precalculated hash value matches, then the binary goes in the `superuser mode`. 

A simple yet resiliant method!

### Examples:
1) **NON SUPER USER** using ***HIDDEN FUNCTION***:
INPUT: ```./binary 1 8 5```
OUTPUT:
```sh
MODES: 
 (1) HIDDEN
 (2) SUM
SELECTED MODE: 1

You are NOT Authenticated
You can only access SUM function
```
2) **NON SUPER USER** using ***SUM FUNCTION***:
INPUT: ```./binary 2 8 5```
OUTPUT: 
```sh
MODES: 
 (1) HIDDEN
 (2) SUM
SELECTED MODE: 2

SUM of 8, 5 = 13
```
3) **SUPER USER (AUTHENTICATED)** using ***HIDDEN FUNCTION***:
INPUT: ```./binary 1 8 5 <PASSWORD>```, where `PASSWORD` is the 'superuser' password
OUTPUT: 
```sh
MODES: 
 (1) HIDDEN
 (2) SUM
SELECTED MODE: 1

HIDDEN FUNCTION of 8, 5 RETURNS <RESULT>
```
> where, `RESULT` is the value computed by the hidden function.

4) **SUPER USER (UN-AUTHENTICATED)** using ***HIDDEN FUNCTION***:
INPUT: ```./binary 1 8 5 <PASSWORD>```, where `PASSWORD` is a WRONG password
OUTPUT: 
```sh
MODES: 
 (1) HIDDEN
 (2) SUM
SELECTED MODE: 1

You are NOT Authenticated
You can only access SUM function
```

5) **SUPER USER** using ***SUM FUNCTION***:
INPUT: ```./binary 2 8 5 <PASSWORD>```, where `PASSWORD` is the 'superuser' password
OUTPUT: 
```sh
MODES: 
 (1) HIDDEN
 (2) SUM
SELECTED MODE: 2

SUM of 8, 5 = 13
```


**Best Wishes H_4_C_|<_!_N_G !**

***Signing Off...***
***Team My5T3r!0u5/-***
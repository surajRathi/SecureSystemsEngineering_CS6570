# CS6570 Assignment 2

## ME19B177 and EE18B110

- The output of the python script should be piped to the input of the binary.
- To run it in GDB, you must first pipe the output to a file, and pipe it to the binary with the ``run`` command.

## Part A:

Exploit generator: [part_a.py](part_a.py)

```bash
./part_a.py | ./lab_2_rop

```

![esctf@osboxes:~/sse/assis/sub2$ ./part_a.py | ./lab_2_rop
Input 10 words:
Here are the first characters from the 10 words concatenated:
6! =
Value in glb is 720
Segmentation fault](img/part_a.png)

## Part B:
Exploit generator: [part_b_caesar.py](part_b.py)  

```bash
./part_b_caesar.py 25 'ABCDEFGHIJKLMNOP' | ./lab_2_rop
```

![img.png](img/part_b.png)

## Reason for Late submission
Before the deadline, we were only aboe 
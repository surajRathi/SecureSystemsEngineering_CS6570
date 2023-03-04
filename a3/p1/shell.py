#! /usr/bin/python3

from connect import connect


def main():
    while True:
        print("Password = ", end='')
        inp = input()
        try:
            password = eval(inp)
        except Exception as e:
            print(f"Your input raised a {e}.")
            print()
            continue

        if password is None:
            break
        try:
            res = connect(password=password)
        except ConnectionResetError:
            print("Connection reset by the server")
            print(f"Your input was: {password}")
            print()
            continue

        print(res)
        print()


if __name__ == '__main__':
    main()

#! /usr/bin/python3

from connect import connect

# import rlcompleter
green = '\001\033[32m\002'
blue = '\001\033[94m\002'
cyan = '\001\033[96m\002'
red = '\001\033[31m\002'
reset = '\001\033[0m\002'


def hist_setup():
    import atexit
    import readline

    hist_file = "./.a3p1_hist"
    try:
        readline.read_history_file(hist_file)
        # default history len is -1 (infinite), which may grow unruly
        readline.set_history_length(-1)
    except FileNotFoundError:
        pass

    atexit.register(readline.write_history_file, hist_file)


def readable_decode(inp: bytes) -> str:
    out = ''
    for byte in inp:
        if 32 <= byte <= 125:
            out += chr(byte)
        else:
            out += f"\\x{byte:02x}"
    return out


def main():
    hist_setup()
    while True:
        try:
            inp = input(f"{green}password = {reset}{blue}")
        except EOFError:
            print(reset, end='')
            break
        print(reset, end='')

        if inp == '':
            continue

        try:
            password = eval(inp)
        except Exception as e:
            print(f"{red}Your input raised a \"{reset}{e}{red}\".{reset}")
            print()
            continue

        if password is None:
            break

        if not isinstance(password, str) and not isinstance(password, bytes):
            print(f"{red}Your input was of type {reset}{type(password)}")
            print(f"{red}Your input was: {reset}{password}")
            print()
            continue

        if isinstance(password, str):
            password = password.encode("ASCII")
        try:
            res = connect(password=password)
        except ConnectionResetError:
            print(f"{red}Connection reset by the server")
            print(f"Your input was: {reset}{password}")
            print()
            continue

        # string_res = res.decode('ASCII')
        string_res = readable_decode(res)

        print(f"{cyan}{string_res}{reset}")
        print()


if __name__ == '__main__':
    main()

#! /usr/bin/python3
import socket

server_ip = '10.21.235.155'
server_port = 1023


def readable_decode(inp: bytes) -> str:
    out = ''
    for byte in inp:
        if (byte == ord(' ')) or \
                (ord('0') <= byte <= ord('9')) or \
                (ord('A') <= byte <= ord('Z')) or \
                (ord('a') <= byte <= ord('z')):
            out += chr(byte)
        else:
            out += f"\\x{byte:02x}"
    return out


def connect(username="test", password="test"):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((server_ip, server_port))
        s.send(username.encode('ASCII'))
        s.send(b'\n')
        s.send(password.encode('ASCII'))
        s.send(b'\n')

        f = s.makefile('rb')
        for i in range(3):
            line = f.readline()

        line = line[line.find(b'?') + 2:]
        line = line[:line.find(b" is not the correct password.")]

        # line = line.decode('ASCII')
        line = readable_decode(line)

        return line


if __name__ == '__main__':
    resp = connect(password="test")
    print(resp)

#! /usr/bin/python3
import socket

server_ip = '10.21.235.155'
server_port = 1023


# Note should the input arguments be bytes?
def connect(username: str = "test", password: str = "test") -> bytes:
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

        return line


if __name__ == '__main__':
    resp = connect(password="test")
    print(resp)
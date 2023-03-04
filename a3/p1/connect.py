#! /usr/bin/python3
import socket

server_ip = '10.21.235.155'
server_port = 1023


def connect(username="test", password="test"):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((server_ip, server_port))
        s.send(username.encode('ASCII'))
        s.send(b'\n')
        s.send(password.encode('ASCII'))
        s.send(b'\n')

        f = s.makefile('r', encoding='ASCII')
        for i in range(3):
            line = f.readline()

        line = line[line.find('?') + 2:]
        line = line[:line.find(" is not the correct password.")]
        # print(f"_{line}_")
        return line


if __name__ == '__main__':
    resp = connect(password="test")
    print(resp)

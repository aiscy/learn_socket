__author__ = 'pavlomv'
import socket


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('www.httpbin.org', 80))
    s.send(b'GET http://httpbin.org/get HTTP/1.0\r\n\r\n')
    print(s.recv(4096))


if __name__ == '__main__':
    main()
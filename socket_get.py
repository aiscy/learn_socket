__author__ = 'pavlomv'
import socket

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('httpbin.org', 80))
    s.send(b'GET /get HTTP/1.1\nHost: www.httpbin.org\n\n')
    recv = s.recv(8192)
    s.close()
    print(recv)


if __name__ == '__main__':
    main()
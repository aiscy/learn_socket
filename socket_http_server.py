__author__ = 'pavlomv'
import socket
import time


def create_header(code):
    header = ''
    if code == 200:
        header = 'HTTP/1.1 200 OK\n'
    elif code == 404:
        header = 'HTTP/1.1 404 Not Found\n'
    elif code == 501:
        header = 'HTTP/1.1 501 Not Implemented\n'
    header += '''Date: {}
                 Server: Nokia3310
                 Connection: close\n\n'''.format(time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime()))

    return header


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 80))
    s.listen(1)
    while True:
        conn, addr = s.accept()
        print('New connection from {}:{}'.format(addr[0], addr[1]))
        data = bytes.decode(conn.recv(1024))
        method = data.split(' ')[0]
        if method == 'GET':
            uri = data.split(' ')[1].split('?')[0]
            if uri == '/':
                uri = '/index.html'
            uri = 'socket_http_server_www' + uri
            print('Requested page is {}'. format(uri))
            try:
                with open(uri, 'rb') as file:
                    content = file.read()
                header = create_header(200)
            except:
                header = create_header(404)
                content = b'<html><body><p>Error 404: File not found</p></body></html>'
        else:
            header = create_header(501)
            content = b'<html><body><p>Error 501: Not Implemented</p></body></html>'
        response = header.encode()
        response += content
        conn.send(response)
        conn.close()
if __name__ == '__main__':
    main()

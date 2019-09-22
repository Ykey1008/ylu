#!/usr/bin/env python
import socket

ADDR = ('0.0.0.0', 80)

RESPONSE = b'''
HTTP/1.1 200 OK

<!DOCTYPE html>
<html>
    <head>
        <title>Hello</title>
    </head>
    <body>
        <h1 style="text-align: center;">Hello World</h1>
    </body>
</html>
'''

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # 建立 SOCK 连接
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # 设置参数
listen_socket.bind(ADDR)                                            # 绑定 IP:端口
listen_socket.listen(100)                                           # 开始监听

print('Server is running: %s:%s ...' % ADDR)

while True:
    client_socket, client_address = listen_socket.accept()  # 接收客户端发起的连接请求
    print('client request from %s:%s' % client_address)
    request = client_socket.recv(1024)

    http_response = RESPONSE

    client_socket.sendall(http_response)
    client_socket.close()

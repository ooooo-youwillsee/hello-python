# coding=utf-8

# 实现简单的http服务器

import simple_socket

#  服务端socket
server_socket = simple_socket.simple_socket()

server_socket.bind(("", 8888))
#  服务端连接数
server_socket.listen(5)

client_socket,client_address = server_socket.accept()

while True:
    recv_data = client_socket.recv(1024)
    if len(recv_data) == 0:
        break
    print(recv_data)

import socket
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect_ex(("10.94.73.86",8081)
client_socket.listen(5)


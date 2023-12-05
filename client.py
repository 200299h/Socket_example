import socket

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
server_address = ('localhost', 8888)
client_socket.connect(server_address)
print('Connected to the server.')

# Receive data from the server
data = client_socket.recv(1024)
print(f'Received from the server: {data.decode("utf-8")}')

# Close the connection
client_socket.close()

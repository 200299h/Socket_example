import socket

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to an address and port
server_address = ('localhost', 8888)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)
print('Server is waiting for connections...')

# Accept a connection
client_socket, client_address = server_socket.accept()
print(f'Connected to {client_address}')

# Send data to the client
message = input()
client_socket.sendall(message.encode('utf-8'))

# Close the connection
client_socket.close()
server_socket.close()
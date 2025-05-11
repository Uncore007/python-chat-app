# Import neccesary modules
import socket
import sys
import time
import threading

# Create socket object
socket_server = socket.socket()
server_host = socket.gethostname()

ip = socket.gethostbyname(server_host)
print("Host IP: ", ip)
server_port = 8080

print("This is your IP address: ", ip)
server_host = input("Enter the friend's IP address: ")

name = input("Enter your name: ")
socket_server.connect((server_host, server_port))

# Retrieve the message from the server
socket_server.send(name.encode())
server_name = socket_server.recv(1024).decode()
print("Server: ", server_name + " has joined the chat.")

def receive_messages():
    while True:
        try:
            message = socket_server.recv(1024).decode()
            print(f"\n{server_name}: {message}")
            print("You: ", end='', flush=True)  # Show prompt again after receiving message
        except:
            print("Connection closed")
            socket_server.close()
            break

def send_messages():
    while True:
        message = input("You: ")
        try:
            socket_server.send(message.encode())
        except:
            break

# Start threads for sending and receiving messages
receive_thread = threading.Thread(target=receive_messages)
receive_thread.daemon = True
receive_thread.start()

send_thread = threading.Thread(target=send_messages)
send_thread.daemon = True
send_thread.start()

# Keep main thread running
while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting chat...")
        socket_server.close()
        break
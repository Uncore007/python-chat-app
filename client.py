# Import neccesary modules
import socket
import sys
import time
import threading

# Create socket object
socket_server = socket.socket()
server_host = socket.gethostname()

# Get the IP address of the server
ip = socket.gethostbyname(server_host)
print("Host IP: ", ip)
server_port = 8080

# Bind the socket to the port
print("This is your IP address: ", ip)
server_host = input("Enter the friend's IP address: ")

# Connect to the server
name = input("Enter your name: ")
socket_server.connect((server_host, server_port))

# Retrieve the message from the server
socket_server.send(name.encode())
server_name = socket_server.recv(1024).decode()
print("Server: ", server_name + " has joined the chat.")

# Function to receive messages from the server
def receive_messages():
    while True:
        try:
            # Receive message from the server
            # If the message is empty, break the loop
            message = socket_server.recv(1024).decode()
            print(f"\n{server_name}: {message}")
            print("You: ", end='', flush=True)  # Show prompt again after receiving message
        except:
            # If an error occurs, or the users disconnects print message and close the connection
            print("Connection closed")
            socket_server.close()
            break

# Function to send messages to the server
def send_messages():
    while True:
        # Get the message from the user
        # If the message is empty, break the loop
        message = input("You: ")
        try:
            # Send the message to the server
            socket_server.send(message.encode())
        except:
            break

# Start threads for sending and receiving messages
receive_thread = threading.Thread(target=receive_messages)
receive_thread.daemon = True
receive_thread.start()

# Start the thread for sending messages
send_thread = threading.Thread(target=send_messages)
send_thread.daemon = True
send_thread.start()

# Keep main thread running
while True:
    try:
        # Keep the main thread alive
        time.sleep(1)
    except KeyboardInterrupt:
        # Handle keyboard interrupt (Ctrl+C)
        print("Exiting chat...")
        socket_server.close()
        break
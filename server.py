# Import neccesary modules
import socket
import sys
import time
import threading

# Create socket object
new_socket = socket.socket()

# Gets current hostname of the server
host_name = socket.gethostname()

# Get the IP address of the server
host_ip = socket.gethostbyname(host_name)
print("Host IP: ", host_ip)
    
# Bind the socket to the port
port = 8080
new_socket.bind((host_ip, port))
print("Socket binded to port: ", port)

# listen for incoming connections
name = input("Enter your name: ")
new_socket.listen(5)

# Accept the connection from the client
connection, address = new_socket.accept()
print("Connection from: ", address)

# Send the name to the client
client = connection.recv(1024).decode()
print("Client: ", client + " has joined the chat.")
connection.send(name.encode())

# Function to receive messages from the client
def receive_messages():
    while True:
        try:
            # Receive message from the client
            # If the message is empty, break the loop
            message = connection.recv(1024).decode()
            print(f"\n{client}: {message}")
            print("Me: ", end='', flush=True)  # Show prompt again after receiving message
        except:
            # If an error occurs, or the users disconnects print message and close the connection
            print("Connection closed")
            connection.close()
            break

# Function to send messages to the client
def send_messages():
    while True:
        # Get the message from the user
        # If the message is empty, break the loop
        message = input("Me: ")
        try:
            # Send the message to the client
            connection.send(message.encode())
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
        # Keep the main thread running to allow sending and receiving messages
        time.sleep(1)
    except KeyboardInterrupt:
        # If the user presses Ctrl+C, break the loop and close the connection
        print("Shutting down server...")
        connection.close()
        new_socket.close()
        break

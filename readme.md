# Overview

This is a simple chat based messaging app written in Python. It was written to demonstrate the principles of socket based networking and concepts relating to chat apps using live services.

To use this app simply clone the repo and run both the server.py and client.py scripts. The server script will provide an IP for connecting the clients to.

This completes three of the given requirments, namely: 

    The client or peer should send a request to the server or another peer. A response should be sent back and used (e.g. displayed)

    You can use either TCP or UDP. (TCP)

    Provide support for at least three different kinds of requests that the server or the peer can respond to. (Connect, Disconnect, Send Message, Receive Message)

[Software Demo Video] (https://youtu.be/aCdJfzmk6uE)

# Network Communication

This app uses a client/server architecture. It utilizes TCP port (specifically port 8080). The messages being sent between the client and server are encoded in UTF-8 plains text strings.

# Development Environment

This tool was written in Python and used a variety of Pyhton modules, including Sys, Socket, Time and Thread

# Useful Websites

* [Python Docs] https://docs.python.org/3/library/socket.html
    
# Future Work

* Increase size limit of messages (currently limited to 1024 bytes)
* Improve the formatting of this app. Currently it uses the commandline which greatly limits the UX of this app
* Create web based server to allow easier connections across the greater internet, securely
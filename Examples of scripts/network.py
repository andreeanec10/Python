#! /usr/bin/python3

import socket
import requests

def check_localhost():
    """Checks if the local host has the right ip address."""
    host = socket.gethostbyname('localhost')
    return "127.0.0.1" == host

def check_connectivity():
    """Checks if the connection is stable."""
    request = requests.get("http://www.google.com")
    return 200 == request.status_code



#for debugging
#print(check_localhost())
#print(check_connectivity())

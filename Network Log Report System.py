# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 09:24:52 2020

@author: Shahazureen Ikwan
"""

import socket
from datetime import datetime

#Set Current Date and Time
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

#Set Network Protocol
#UDP_IP = "127.0.0.1"
UDP_IP = "10.61.10.85"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((UDP_IP,UDP_PORT))

while True:
    data,addr = sock.recvfrom(1024)

    condition = str(data)
    
    
    if condition == "b'User'":
        print ("\nGuest is connected to server at ",dt_string)
        
    elif condition == "b'Userlogout'":
        print ("\nUser has log out at ", dt_string)
        
    elif condition == "b'Administrator'":
        print ("\nAdmin is connected to the server at ",dt_string)
        
    elif condition == "b'Adminlogout'":
        print ("\nAdmin has log out at ",dt_string)
        
    elif condition == "b'AdminADDdatabase'":
        print ("\nAdmin has added database at ",dt_string)
        
    elif condition == "b'AdminADDdoc'":
        print ("\nAdmin has added document at ",dt_string)
        
    elif condition == "b'AdminUPDATEdoc'":
        print ("\nAdmin has updated a document at ", dt_string)
        
    elif condition == "b'AdminDELdoc'":
        print ("\nAdmin has deleted a document at ", dt_string)
        
    else:
        pass
    

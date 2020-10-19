#! /usr/bin/env python3

from encapFramedSock import EncapFramedSock

# Echo client program
import socket, sys,os, re, params
sys.path.append("../lib")       # for params

switchesVarDefaults = (
    (('-s', '--server'), 'server', "127.0.0.1:50020"),
    (('-?', '--usage'), "usage", False), # boolean (set if present)
    )


progname = "framedClient"
paramMap = params.parseParams(switchesVarDefaults)

server, usage  = paramMap["server"], paramMap["usage"]

if usage:
    params.usage()

try:
    serverHost, serverPort = re.split(":", server)
    serverPort = int(serverPort)
except:
    print("Can't parse server:port from '%s'" % server)
    sys.exit(1)

addrFamily = socket.AF_INET
socktype = socket.SOCK_STREAM
addrPort = (serverHost, serverPort)

s = socket.socket(addrFamily, socktype)
if s is None:
    print('could not open socket')
    sys.exit(1)

s.connect(addrPort)

encapSock = EncapFramedSock((s,addrPort))
#needs to be the file we read from

fileName = input("File you want to send: ")
# print(fileName, "This is test")

if os.path.exists(fileName):#if file exists on client end
    inputFile = open(fileName, mode = "r", encoding="utf-8")    
    fileStuff = inputFile.read()
    
    if len(fileStuff) == 0:
        print('will not send empty file exiting')
        sys.exit(0)#don't send an empty file
        
    print("sending file")
    encapSock.send(fileName,fileStuff, debug = 1)
encapSock.close()#close socket after sending file



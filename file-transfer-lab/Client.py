#! /usr/bin/env python3

from framedSock import framedSend, framedReceive

# Echo client program
import socket, sys,os, re, params
sys.path.append("../lib")       # for params

switchesVarDefaults = (
    (('-s', '--server'), 'server', "127.0.0.1:50001"),
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

if s is None:
    print('could not open socket')
    sys.exit(1)
#needs to be the file we read from
fileName = input("File you want to send: ")
print(fileName, "This is test")
if os.path.exists(fileName):#if file exists on client end
    inputFile = open(fileName, mode = "r", encoding="utf-8")    
    fileStuff = inputFile.read()
    if len(fileStuff) == 0:
        print('will not send empty file exiting')
        sys.exit(0)
    framedSend(s,fileName.encode(), debug = 1)
    exists = framedReceive(s, 1)
    if exists:
        print('file already in server')
        sys.exit(0)
    else:
        fileStuff +="!:!"
        try:
            framedSend(s,fileStuff,1)
        except:
            print('Error occured while sending, check connection')
            sys.exit(0)
        try:
            framedReceive(s,1)
        except:
            print('error while recieving')
            sys.exit(0)
else:
    print("File does not exist, exiting now....")
    sys.exit(0)

print("sending file")
framedSend(s, fileStuff)


# print("sending stuff" % outMessage)
# sendAll(s, fileStuff)

s.shutdown(socket.SHUT_WR)      # no more output

while 1:
    data = s.recv(1024).decode()
    print("Received '%s'" % data)
    if len(data) == 0:
        break
print("Zero length read.  Closing")
s.close()
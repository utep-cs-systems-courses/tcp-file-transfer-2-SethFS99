Client.py--
Can be ran anywhere, however it should be accompanied with some txt files to show it can transfer files. Client.py will NOT send any empty files to the sever. Will end after sending the file

encapFramedSock.py and params.py is are helper files that both Client and Sever should have a copy of at all times in order to run.

Server.py--should be run in a different file location that the client in order to properly demonstrate how it works, you should contain the server in another folder separate from Client.py.
 The server will recieve any file sent to it and store it in the same file location, it will not accept duplicate file names, regardless of what's contained in them.
 The server will create multiple threads to recieve files from multiple clients. 
 The server can recieve several files at once, however it can only write to one file at a time.

Yeah not much too this one, I tried

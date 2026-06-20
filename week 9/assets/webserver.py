from socket import *
import sys

serverSocket = socket(AF_INET, SOCK_STREAM)

serverPort = 6789
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print(f"Server ready on port {serverPort}...")

while True:
    print('Ready to serve...')
    
    connectionSocket, addr = serverSocket.accept()
    
    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        filename = filename[1:]  # Remove leading /
        print(f"Requested: {filename}")
        
        f = open(filename)
        outputdata = f.read()
        f.close()
        
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/html\r\n".encode())
        connectionSocket.send(f"Content-Length: {len(outputdata)}\r\n".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.send(outputdata.encode())
        connectionSocket.close()
        
    except IOError:
        # Send 404 response
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n".encode())
        connectionSocket.send("Content-Type: text/html\r\n".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.send("<html><body><h1>404 Not Found</h1></body></html>\r\n".encode())
        connectionSocket.close()

serverSocket.close()
sys.exit()
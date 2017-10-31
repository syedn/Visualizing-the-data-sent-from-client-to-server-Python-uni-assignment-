import socket
import json

frequency = {}
text = open('sample.txt', 'r').read()

for character in text:
    count = frequency.get(character,0) #get() counts the number of times key appeared in dictionary and returns the value 
    frequency[character] = count + 1
    
jsonData = json.dumps(frequency) #decode the whole dictionary into json
#INET socket = internet sockets that use IP protocol and ports
#SOCK_STREAM socket = TCP socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creates a socket
clientHost = socket.gethostname()
clientPort = 8123
clientSocket.connect((clientHost, clientPort)) #connect client to host and port (socket)
clientSocket.send(str(jsonData).encode()) #encode strings into byte-like objects and send data to server
response = clientSocket.recv(1024) #recieves response from server
print(response)
clientSocket.close() 


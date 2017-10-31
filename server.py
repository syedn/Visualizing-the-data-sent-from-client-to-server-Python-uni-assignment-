import socket
import json
import matplotlib.pyplot as pygraph

serverSocket = socket.socket(socket.AF_INET , socket.SOCK_STREAM) #creates a socket
serverHost = socket.gethostname()
serverPort = 8123
serverSocket.bind((serverHost, serverPort))
serverSocket.listen(2) #make a server socket
print("Server running and listening to requests!")
connection , address = serverSocket.accept() #accept incoming connections
if True: #if connection is built successfully 
    jsonData = connection.recv(1024) #recieve data from client
    frequency = json.loads(jsonData.decode())  
    print("Output:\n")
    #####################################################
# Set figure width to 12 and height to 9
pygraph.rcParams["figure.figsize"] = 12,9 
    #####################################################
# Histogram representation of data
print("Characters ", " Frequency")
for key in frequency:
        print(key,"\t    ",frequency[key])
pygraph.title("Frequency Distribution Histogram")
pygraph.xlabel("Characters")
pygraph.ylabel("Frequencies")
pygraph.bar(range(len(frequency)), frequency.values(), align='center') #(x,y,align bars)
pygraph.xticks(range(len(frequency)), frequency.keys())   #(number of ticks, ticks to be printed)  
pygraph.show()  

    #####################################################

#Ranked distribution representation of data 
rankedFreq = {}
for rankKey in sorted(frequency, key=frequency.get,reverse=True): #sort frequencies
  rankedFreq[rankKey] = frequency[rankKey]
print("Ranking ","Characters ", "Frequency")
rank = 1
for key in rankedFreq:
        print(rank," \t ",key,"\t    ",rankedFreq[key])
        rank+=1


pygraph.title("ranked Distribution ")
pygraph.xlabel("Characters")
pygraph.ylabel("Frequency")
rankBar = pygraph.bar(range(len(rankedFreq)), rankedFreq.values(), align='center')
# Add counts above the bar graphs
for barValue in rankBar:
    height = barValue.get_height()
    pygraph.text(barValue.get_x() + barValue.get_width()/2.0, height, '%d' % int(height), ha='center', va='bottom')
pygraph.xticks(range(len(rankedFreq)), rankedFreq.keys())
pygraph.show()  
   
    
    
    #####################################################
#probablity distribution representation of data
freqSum = sum(frequency.values()) 
print("Characters ", " Probablity")
probArray = {} #store probablities of all frequencies
for key in frequency:
    probArray[key] = frequency[key]/freqSum #probablity of each frequency
    print(key,"\t    ",round(probArray[key],4))
pygraph.title("Probablity Distribution ")
pygraph.xlabel("Characters")
pygraph.ylabel("Probablity")
pygraph.bar(range(len(probArray)), probArray.values(), align='center')
pygraph.xticks(range(len(probArray)), probArray.keys())    
pygraph.show()  
    
    ###################################################
answer = "Your Request Has Been Successfully Processed"
connection.sendall(answer.encode()) #send response to client
    
connection.close()
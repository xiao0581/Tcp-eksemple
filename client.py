from socket import *
import json
serverName="127.0.0.1"
serverPort=30303
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort)) 
while True: 
        id = input("id:")
        ppm = input("ppm:")       
        request = {"id":id,"ppm":ppm}
        message = json.dumps(request)
        clientSocket.send(message.encode())
        respose=clientSocket.recv(1024).decode()
        respose_jason=json.loads(respose)
        print(respose_jason)           
       
        closeMessage=input("Type exit to close or press enter to continue:")
        if closeMessage.strip().lower() == "exit":
                break    
clientSocket.close()                         
        
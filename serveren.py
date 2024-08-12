from socket import*
import json
import threading
import random
ip=""
serverPort=30303
Server=socket(AF_INET,SOCK_STREAM)
Server.bind((ip,serverPort))
Server.listen(3)
co2 = [{"id":1,"ppm":850},{"id":5,"ppm":1033},{"id":1,"ppm":705}]
print("Server ready for recive info")
def handle(connectionSocket,addr):
       try:   
            sentence = connectionSocket.recv(1024).decode()
            request= json.loads(sentence)
            print("new co2 fra client :"+str(request))
            co2.append(request)
            connectionSocket.send(json.dumps(co2).encode())
            print(co2)
            
       except json.JSONDecodeError as e:
              print(" Invalid Json format ", str(e))
       except Exception as e:
              print(" Client disconnect or exception occurred ", str(e))
       finally:
              connectionSocket.close()
while True:
    connectionSocket, addr = Server.accept()
    threading.Thread(target = handle,args = (connectionSocket,addr)).start()
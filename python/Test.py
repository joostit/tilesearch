from TcpServer import TcpServer
from time import sleep

print("Running Tester")

server = TcpServer()
server.start()

while True:
    sleep(2)
#    print("Sending test")
#    server.send("Shouting TEST!!!!!!")

print("Ended Tester")
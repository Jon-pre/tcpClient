# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from socket import *

hostname = '127.0.0.1'
serverPort = 12000
clientsocket = socket(AF_INET, SOCK_STREAM)
clientsocket.connect((hostname, serverPort))
while True:
    sentence = input("Skriv inn noe her: ")
    clientsocket.send(sentence.encode())
    modifiedSentence = clientsocket.recv(1024)
    if modifiedSentence.decode() == "EXIT":
        clientsocket.close()
    print("From server: ", modifiedSentence.decode())




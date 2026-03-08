import socket
import threading

HOST = '127.0.0.1'
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

name = input("Enter your name: ")

def receive():
    while True:
        try:
            message = client.recv(1024).decode()
            print(message)
        except:
            print("Connection closed")
            client.close()
            break

def write():
    while True:
        message = f"{name}: {input('')}"
        client.send(message.encode())

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
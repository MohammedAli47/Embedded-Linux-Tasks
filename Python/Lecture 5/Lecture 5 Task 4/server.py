from socket import *
from threading import *

#count = 0

def new_client(client, address):
    #global count
    #count += 1
    rodata = client.recv(1024)
    print(f"Client {address} sending: {rodata.decode('UTF-8')}")
    client.sendall(b"\nMessage delivered")
    client.close()


with socket(AF_INET, SOCK_STREAM) as server:
    ip = gethostbyname(gethostname())
    print(gethostname())
    print("IP: " + ip)
    server.bind((ip, 5000))
    server.listen(5)
    while True:
        client, address = server.accept()
        thread = Thread(target=new_client, args=(client, address))
        thread.start()

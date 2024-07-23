from socket import *

ip = gethostbyname(gethostname())
print("IP: " + ip)
while True:
    client = socket(AF_INET, SOCK_STREAM)
    client.connect((ip, 5000))
    message = str(input("Enter message: ")).encode("UTF-8")
    client.sendall(message)
    rodata = client.recv(1024)
    print(f"Server {ip} sending: {rodata.decode('UTF-8')}")
    client.close()

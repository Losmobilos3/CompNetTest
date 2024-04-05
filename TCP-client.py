import socket as s
import sys

tcpClient = s.socket(s.AF_INET, s.SOCK_STREAM)

if __name__ == "__main__":
    address = sys.argv[1]
    port = int(sys.argv[2])

serverAddress = (address, int(port))

tcpClient.connect(serverAddress) # Siger at vores klient skal connecte til denne addresse

print(tcpClient.recv(32).decode('utf-8'))

tcpClient.close()
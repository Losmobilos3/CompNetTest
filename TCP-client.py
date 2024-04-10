import socket as s
import sys

tcpClient = s.socket(s.AF_INET, s.SOCK_STREAM)

if __name__ == "__main__":
    address = sys.argv[1]
    port = int(sys.argv[2])

serverAddress = (address, int(port))

tcpClient.connect(serverAddress) # Siger at vores klient skal connecte til denne addresse

print(int.from_bytes(tcpClient.recv(4)))

tcpClient.close()
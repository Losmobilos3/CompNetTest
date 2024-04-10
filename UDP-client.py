import socket as s
import sys

if __name__ == "__main__":
    address = sys.argv[1]
    port = int(sys.argv[2])

udpClient = s.socket(s.AF_INET, s.SOCK_DGRAM)

serverAddress = (address, port)

udpClient.sendto(b'', serverAddress)

message = int.from_bytes(udpClient.recv(4))

udpClient.close()

print(message)
import socket as s
import sys

if __name__ == "__main__":
    address = sys.argv[1]
    port = int(sys.argv[2])

udpClient = s.socket(s.AF_INET, s.SOCK_DGRAM)

serverAddress = (address, port)

udpClient.sendto(b'', serverAddress)

#bytearray("", 'utf-8')

message = udpClient.recv(32).decode('utf-8')

udpClient.close()

print(message)
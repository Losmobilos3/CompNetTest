import socket as s
import select as sel
import time
import sys

if __name__ == "__main__":
    port = sys.argv[1]

address = s.gethostbyname(s.gethostname())

serverAddress = (address, int(port))


tcpServer = s.socket(s.AF_INET, s.SOCK_STREAM)
udpServer = s.socket(s.AF_INET, s.SOCK_DGRAM)

tcpServer.bind(serverAddress)
udpServer.bind(serverAddress)

tcpServer.listen()

while True:
    rlist, _, _ = sel.select([tcpServer, udpServer], [], [], 1)

    for socket in rlist:
        if socket == tcpServer:
            tcpClient, address = tcpServer.accept()
            print(f"Connected to {address}")
            tcpClient.send(str(int(time.time() + 2208988800)).encode('utf-8'))
            tcpClient.close()

        if socket == udpServer:
            _, sourceAddress = udpServer.recvfrom(0)
            udpServer.sendto(str(int(time.time() + 2208988800)).encode('utf-8'), sourceAddress)
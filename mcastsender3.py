from __future__ import print_function
import socket
from datetime import datetime
import time
from contextlib import closing

LOCAL_ADDR = '127.0.0.1'
MCAST_GRP = '239.255.0.1'
MCAST_PORT = 4001
MESSAGE_COUNT = 0

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_LOOP, 0)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 32)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_IF, socket.inet_aton(LOCAL_ADDR))
#setsockopt 3 argument, some sock.setsockopt can be done

while True:
    MESSAGE = 'MulticastMessage:{0}:'.format(MESSAGE_COUNT).encode('utf-8')
    SEND_TIME = datetime.now().strftime("%Y:%m:%d:%H:%M:%S.%f") 
    DATA = MESSAGE + SEND_TIME
    print(DATA)
    sock.sendto(DATA, (MCAST_GRP, MCAST_PORT))
    MESSAGE_COUNT = MESSAGE_COUNT + 1
    time.sleep(0.5)


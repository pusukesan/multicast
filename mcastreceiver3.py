from __future__ import print_function
from datetime import datetime
import socket
from contextlib import closing

def main():
  local_address   = '127.0.0.1' #IP address on receiver
  multicast_group = '239.255.0.1' #multicast address
  port = 4001
  bufsize = 4096
  #downtime = 0
  #downtime_before = 0
  downcount = 0

  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  sock.bind(('', port))
  sock.setsockopt(socket.IPPROTO_IP,
                  socket.IP_ADD_MEMBERSHIP,
                  socket.inet_aton(multicast_group) + socket.inet_aton(local_address))
  sock.settimeout(1)

  while True:
    try:
      hoge = sock.recv(bufsize)
      rcv_time = datetime.now().strftime("%Y:%m:%d:%H:%M:%S.%f")
      print(hoge.decode('utf-8') +":"+ rcv_time)
      downcount = 0
    except socket.timeout:  
      downcount += 1
      print("down " + str(downcount) +"sec")
      
  return

if __name__ == '__main__':
  main()

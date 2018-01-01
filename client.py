import socket
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
command = raw_input("enter your command")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(command)
data = s.recv(BUFFER_SIZE)
s.close()
print "received data:", data 
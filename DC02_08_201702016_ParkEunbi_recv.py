import socket

server_IP ='192.168.0.103'
#server_IP = '127.0.0.1'
server_Port = 2500

server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server_sock.bind((server_IP, server_Port))

data_size = 0
trans_rate = 0
recv_data = 0
print("file recv start from ", server_IP)

data, addr = server_sock.recvfrom(2000)
f = open(data.decode(), 'wb')
print("File Name: ", data)
data, addr = server_sock.recvfrom(2000)
data_size = int(data.decode())
print("File Size: ", data_size)


while True:
	data, addr = server_sock.recvfrom(2000)
	if data == b'':
		print("file_recv_end")
		f.close()
		server_sock.close()
		break
	f.write(data)
	recv_data += len(data)
	trans_data = (recv_data/data_size)*100
	print("current_size / total_size = ", recv_data, "/", data_size, trans_data, "%")


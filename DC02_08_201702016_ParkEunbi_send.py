import socket
import os.path

client_IP = '192.168.0.103'
#client_IP = '127.0.0.1'
client_PORT = 2500
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
data = input("Input your file name: ")
sock.sendto(data.encode(),(client_IP, client_PORT))
data_size = os.path.getsize(data)
sock.sendto(str(data_size).encode(),(client_IP,client_PORT))
#print(data_size)
f = open(data, 'rb')
send_data = 0
	
while True:
	data = f.read(1024)
	if data == b'':
		sock.sendto(data, (client_IP, client_PORT))
		print("ok")
		print("file_send_end")
		f.close()
		sock.close()
		break
	send_data += sock.sendto(data, (client_IP, client_PORT))
	trans_rate = (send_data/data_size)*100
	print("current_size / total_size = " , send_data , "/" , data_size, trans_rate , "%")


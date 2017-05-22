#!/usr/bin/python3

import socketserver
import socket

class SocketHandler(socketserver.BaseRequestHandler):
	def handle(self):
		while True:
			self.data=self.request.recv(1024).strip()
			print("{} wrote:".format(self.client_address[0]))
			print(self.data)
			#re=input("Please enter : ")
			self.request.sendall(b"Hello\n")
			if self.data=="bye":
				break
		

	def tanslate(self,tdata,thost,tport=80):
		self.trasocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.trasocket.connect((thost,tport))
		self.trasocket.sendall(bytes(tdata,"utf-8"))
		return self.trasocket.recv(1024)


if __name__ == '__main__':
	host,port="localhost",7575
	server=socketserver.TCPServer((host,port),SocketHandler)
	server.serve_forever()
	# with socketserver.TCPServer((host,port),SocketHandler) as s:
	# 	s.server_forever()
import socket 
import sys
import select
import errbug

errbug.isDebugging = 1;
def main():
	try:
		serv_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	except socket.error, msg:
		errbug.fatal(msg)
		
	host = socket.gethostname() 
	port = 12345
	try:
		serv_sock.bind((host, port))
	except socket.error, msg:
		errbug.fatal(msg)
	
	serv_sock.listen(1)
	input = [serv_sock]
	while 1:
		input_chk, out_chk, err_chk = select.select(input,[],[])
		for j in input_chk:
			if j == serv_sock:
				client, addr = j.accept()
				errbug.debug("Connection")
				input.append(client)
			else:
				data = j.recv(1024)
				if data == '':
					errbug.debug('Conection closed...')
					j.close()
					input.remove(j)
				else:
					errbug.debug('Recieved: %s'%data)
					j.send("Echo - %s"%data)
					errbug.debug('Sent reply.')
	s.close
	
if __name__ == "__main__":
	main()

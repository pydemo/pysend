import socket               # Import socket module
import sys, time
class NetcatWriter:
	def __init__(self, port,client_name):
		print '__init__'
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
		#s.setsockopt(socket.IPPROTO_TCP, socket.TCP_CORK, 1)
		self.s.setblocking(False)
		self.s.settimeout(2)
		self.host = 'jc1lbiorc1p'
		self.port = port
		self.client_name=client_name
		self.s.connect((self.host, self.port))
	def __enter__(self):
		print '__enter__'
		return self
	def write(self,msg):
		print 'Sending..',
		l = 'client:%s --%s--'  % (self.client_name,msg)
		while (l):
			print '.',
			self.s.send(l)
			l=None
		#f.close()
		print "Done Sending"
		#
	def __exit__(self, exc_type, exc_value, traceback):
		self.s.shutdown(socket.SHUT_WR)
		self.s.close
client_name='file_writer_123467'
#netcat= NetcatWriter(12347,client_name)
e=sys.exit
#s = socket.socket()         # Create a socket object
s= socket.socket(socket.AF_INET, type=socket.SOCK_STREAM, proto=0)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
#s.setsockopt(socket.IPPROTO_TCP, socket.TCP_CORK, 1)
host = socket.gethostname() # Get local machine name
port = 12348                 # Reserve a port for your service.
print port
s.bind((host, port))        # Bind to the port
f = open('C:\\Temp\\example_lines.txt','wb')
s.listen(5)                 # Now wait for client connection.
i=0
while True:
	c, addr = s.accept()     # Establish connection with client.
	c.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	c.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
	#c.setsockopt(socket.IPPROTO_TCP, socket.TCP_CORK, 1)
	print 'Got connection from', addr
	print "Receiving..."
	#netcat.write('netcat from file writer')
	i=0
	l = c.recv(100*1024)
	print len(l)
	#f.write(l)
	#f.close()
	while (l):
		#print "*",
		#if i%10000==0:
		#		netcat.write('Chunk# %d' % i)
		#f = open('/tmp/torecv_%d.png' % i,'wb')
		f.write(l)
		#f.close()
		l = c.recv(100*1024)
		i +=1
		if 0 and i>20:
			f.close()
			e(0)
	f.close()

	#c.send('Thank you for connecting')
	c.close()
	#s.shutdown(socket.SHUT_WR)
	s.close()
	print "Done Receiving"
	#del netcat
	e(0)
e(0)


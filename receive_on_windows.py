import socket  # Import socket module
import sys, time
from pprint import pprint
e=sys.exit
try:
	import cPickle as pickle
except:
	import pickle

try:
	import cStringIO
except ImportError:
	import io as cStringIO
	
	
def netcat_read_messages(**kargs):
	host, port = kargs['host'], kargs['port']
	#s = socket.socket()         # Create a socket object
	timed_out=True
	output = cStringIO.StringIO()
	while timed_out:
		try:
			print 1
			s= socket.socket(socket.AF_INET, type=socket.SOCK_STREAM, proto=0)
			s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
			s.setblocking(False)
			s.settimeout(1)
			#timed_out=False
			print 2

				
					
			
			#s.settimeout(10)
			#s.setsockopt(socket.IPPROTO_TCP, socket.TCP_CORK, 1)
			#host = socket.gethostname() # Get local machine name
			#port = port                 # Reserve a port for your service.
			print port
			s.bind((host, port))        # Bind to the port
			#f = open('C:\\Temp\\example_lines.txt','wb')
			s.listen(5)                 # Now wait for client connection.
			i=0
			while True:
				c, addr = s.accept()     # Establish connection with client.
				c.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
				c.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
				c.setblocking(False)
				c.settimeout(1)
				#c.setsockopt(socket.IPPROTO_TCP, socket.TCP_CORK, 1)
				print 'Got connection from', addr
				print "Receiving..."
				#netcat.write('netcat from file writer')
				i=0
				l = c.recv(100*1024)
				if 1:
					#datastream = src.getvalue()
					#print repr(l)
					#dst = cStringIO.StringIO(l)
					print >>output, l
					print pickle.loads(output.getvalue())
					#up = pickle.Unpickler(dst)
				#print l
				#print pickle.loads(l)
				#f.write(l)
				#f.close()
				while (l):
					#print "*",
					#if i%10000==0:
					#		netcat.write('Chunk# %d' % i)
					#f = open('/tmp/torecv_%d.png' % i,'wb')
					#f.write(l)
					#f.close()
					l = c.recv(100*1024)
					try:
						#print pickle.loads(l)
						#print repr(l)
						#dst = cStringIO.StringIO(l)
						#up = pickle.Unpickler(dst)
						#pprint(dir(up))
						#e()
						#output.write(l)
						print >>output, l
						print pickle.loads(output.getvalue())
						#print contents
						
					except:
						pprint(l)
						raise
						
					#print l
					i +=1
					if 0 and i>20:
						f.close()
						e(0)
				#f.close()

				#c.send('Thank you for connecting')
				c.close()
				#s.shutdown(socket.SHUT_WR)
				#s.close()
				print "Done Receiving"
				#del netcat
				#e(0)
			#f.close()
			s.close()
		except socket.timeout, er1:
			err = er1.args[0]
			pprint(er1.args)
			print '-----socket.timeout'
			timed_out=True
			#f.close()
			s.close()
			#raise er1			
		except socket.error, er3:
			err = er3.args[0]
			print er3.args 			
			#f.close()
			s.close()
			timed_out=False
			raise er3
	

if __name__ == '__main__':
	netcat_read_messages(host=socket.gethostname(), port=12348)

import threading
import datetime

class ThreadClass(threading.Thread):
	def run(self):
		for _ in range(10):
			now = datetime.datetime.now()
			print("%s says Hello World at time: %s" % (self.getName(), now))


send = ThreadClass()
receive = ThreadClass()

send.start()
receive.start()
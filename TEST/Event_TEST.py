import threading

eve = threading.Event()

class PrepareThread(threading.Thread):
	def run(self):
		eve.set()
		print('Ready to NEXT')

class ActionThread(threading.Thread):
	def run(self):
		print("%s Watiting..." % self.getName())
		eve.wait()
		print("%s Done..." % self.getName())

threads = []

for i in range(100):
	threads.append(ActionThread())

for th in threads:
	th.start()

th2 = PrepareThread()
th2.start()
th2.join()

for th in threads:
	th.join()

print("Finish All of the Work")
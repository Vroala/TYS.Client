import threading, time

sem = threading.Semaphore(3)

class RestrictedArea(threading.Thread):
	def run(self):
		for x in range(3):
			msg = 'Threading Semaphore TEST : %s' % self.getName()
			sem.acquire()
			print("[%s] %s" % (time.ctime(), msg))
			time.sleep(2)
			sem.release()

threads = []

for i in range(5):
	threads.append(RestrictedArea())

for th in threads:
	th.start()

for th in threads:
	th.join()

print("Finish All Threading")
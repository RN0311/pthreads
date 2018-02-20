# Threads in python
### What is threading?
> In Computer Science, threads are light-weight process.
> * Threads exists inside a process.
> * Multiple threads can exist in a single process.
> * Threads in same process share the state and memory of the parent process.
> * Useful when an application wants to perform many concurrent tasks on shared data.

Python's thread module provides low-level access to threads
* Thread creation.
* Simple mutex locks.

Major components of Threading module are:
* Thread object.
* Lock object.
* RLock object.
* Semaphore object.
* Condition object.
* Event object.


Let's understand creation of a new thread, using below code snippet.
###### ```threading``` 
```Python
from threading import thread
import time

def nap_time(i):
  print("Thread %i taking a short nap",%i)
  time.sleep(2)
    print("Thread %i is up now." % i)
for i in range(5):
    th = Thread(target=nap_time, args=(i, ))
    th.start()   ''' this starts the thread '''    
```
When you run the above program, the output might be different as parallel threads doesn’t have any defined order of their life.
###### ```threading.enumerate()``` and ```threading.activeCount()```
```Python 
import threading
import time
import random

def executeThread(i):
	print("Thread {} sleeps at {}".format(i,time.strftime("%H:%M:%S",time.gmtime())))


	randomSleepTime = random.randint(1,5);
	time.sleep(randomSleepTime);

	print("Thread {} stops sleeping at {}".format(i,time.strftime("%H:%M:%S",time.gmtime())))


	for i in range(1):
		thread = threading.Thread(target=executeThread,args=(i,))
		thread.start()

		print("Active Threads :",threading.activeCount());
		print("Thread Objects :",threading.enumerate());


executeThread(2)
```
This time, we will have new output showing list of how many threads are active at various timestamps.
 
###### ```threading.timer```   
```Python
import threading

def time_delay():
    print("Oh,I've to wait & then printed after 5 seconds!")

thread = threading.Timer(5, time_delay)
thread.start()
```
###### ```threading.is_alive()``` and ```threading.getName()``` and ```threading.join()```
```Python
import threading
import time
import random
class CustThread(threading.Thread):
	def __init__(self,name):
		threading.Thread.__init__(self)
		self.name = name

	def run(self):
		getTime(self.name)
		print("Thread",self.name,"Execution Ends")
def getTime(name):
	print("Thread {} sleeps at {}".format(name,time.strftime("%H:%M:%S",time.gmtime())))
	randSleepTime = random.randint(1,5);
	time.sleep(randSleepTime);

thread1 = CustThread("1")
thread2 = CustThread("2")

thread1.start()
thread2.start()

print("Thread 1 is alive : ",thread1.is_alive())
print("Thread 2 is alive : ",thread2.is_alive())

print("Thread 1 Name : ",thread1.getName())
print("Thread 2 Name : ",thread2.getName())

thread1.join()
thread2.join()

print("Execution Ends")
```
This program, returns the name of thread and states that whether it is active or not, before printing Execution Ends!. 

## How is thread terminated?
> * Thread silently exits when the function returns.
> * Thread can explicitly exit by calling thread.exit() or sys.exit().
> * Uncaught exception causes thread termination.

Python's thread can also, be used to acquire locks.
<br >
* ```allocate_locks``` : Creates a lock object, initially unlocked.
```Python
import thread
locked_thread = thread.allocate_lock()
def foo():
 ''' Acquire the lock '''
`locked_thread.acquire() 

 ''' critical section '''
 ''' Release the lock '''
 
 locked_thread.release() 
```
* Only one thread can acquire a lock at once.
* Threads block indefinitely until lock becomes available.

Example : There are multiple bank accounts of some people, we need to monitor others so that they don't withdraw more money than their bank-balance. Let's do this example using locks in python.
```Python

import threading
import time
import random


class BankAccount(threading.Thread):
	acctBalance = 100
	def __init__(self,name,moneyRequest):
		threading.Thread.__init__(self)

		self.name = name
		self.moneyRequest = moneyRequest

	def run(self):
		threadLock.acquire()
		BankAccount.getMoney(self)

		threadLock.release()


	@staticmethod
	def getMoney(customer):
		print("{} tries to withdraw ${} at {}".format(customer.name,customer.moneyRequest,
			time.strftime("%H:%M:%S",time.gmtime())))

		if BankAccount.acctBalance - customer.moneyRequest > 0:
			BankAccount.acctBalance -= customer.moneyRequest
			print("New account balance : ${}".format(BankAccount.acctBalance))
		else:
			print("Not enough money in account")
			print("Current balance : ${}".format(BankAccount.acctBalance))
		time.sleep(3)

threadLock = threading.Lock()

frank = BankAccount("Frank",10)
Mary = BankAccount("Mary",100)
Jass = BankAccount("Jass",50)

frank.start()
Mary.start()
Jass.start()

frank.join()
Mary.join()
Jass.join()

print("Execution Ends!")
```

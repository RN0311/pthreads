'''
lock out someone else to withdraw money from your account
'''
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


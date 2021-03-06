from queue import PriorityQueue 
#make sure this line is in the top of your code 

class priority_queue:
	def __init__(self):
		self.__q = PriorityQueue()
		self.__size = 0
	#done
	def size(self):
		return self.__size
	#done
	def front(self):
		x = self.__q.get()
		self.__q.put(x)
		return x[0]
	#done
	def insert(self,x):
		self.__q.put((x,x))
		self.__size+=1
	#done
	def empty(self):
		if(self.__size == 0):
			return 1
		else:
			return 0
		#done
	#done
	def clear(self):
		self.__q.clear()
		self.__size = 0
	#done
	def pop(self):
		if(self.__size > 0):
			x = self.__q.get()
			self.__size-=1;
			del x
			return
		else:
			print("Queue has no data")
			sys.exit(-1)
		#done
	#done
#done

def main():
	asif = priority_queue()
	asif.insert(5)
	asif.insert(4)
	asif.insert(5)
	asif.insert(7)
	asif.insert(1)

	print(asif.front())
	asif.pop()
	print(asif.front())
	print(asif.size())

main()

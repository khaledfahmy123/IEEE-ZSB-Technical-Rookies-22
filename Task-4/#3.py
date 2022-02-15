class Node(object):
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList(object):
	def __init__(self, head=None):
		self.head = head
		self.counter = 0

	def print_list(self):
		if self.head == None:
			raise ValueError("List is empty")
		current = self.head 
		while(current):
			print (current.data, end="  ")
			current = current.next
		print ('\n')


	## insert at a position
	def push_at(self, newElement, position):
		newNode = Node(newElement) 
		if(position < 1):
			print("\nposition should be >= 1.")
		elif (position == 1):
			newNode.next = self.head
			self.head = newNode
		else:
			temp = self.head
			for i in range(1, position-1):
				if(temp != None):
					temp = temp.next   
			if(temp != None):
				newNode.next = temp.next
				temp.next = newNode
			else:
				print("\nThe previous node is null.")

	def deleteNode(self, key):
		
		temp = self.head
		
		if (temp is not None):
			if (temp.data == key):
				self.head = temp.next
				temp = None
				return

		while(temp is not None):
			if temp.data == key:
				break
			prev = temp
			temp = temp.next

		if(temp == None):
			return

		prev.next = temp.next
		temp = None

	def count(self, li, key):

		if(not li):
			return self.counter

		if(li.data == key):
			self.counter = self.counter + 1

		return self.count(li.next, key)





lol = LinkedList(Node(1))
lol.print_list()
lol.push_at(6, 2)
lol.push_at(5, 3)
lol.push_at(6, 4)
lol.push_at(6, 5)
lol.print_list()
lol.deleteNode(6)
lol.print_list()
print(f"the value repeated : {lol.count(lol.head, 6)} times")
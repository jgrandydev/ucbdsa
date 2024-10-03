
# singly linked list

import math


class SingleSidedNode:

	def __init__(self, data):
		self.data = data
		self.next_node = None


class SinglyLinkedList:

	def __init__(self, value):
		node = SingleSidedNode(value)
		self.first_node = node
		self.last_node = node
		self.count = 1


	def count(self):
		return self.count
	

	def count_nodes(self):
		current_index = 0
		current_node = self.first_node
		while(current_node):
			current_node = current_node.next_node
			current_index += 1
		return current_index


	def read_node(self, target_index):
		current_index = 0
		current_node = self.first_node
		while(current_index < target_index):
			current_node = current_node.next_node
			if not current_node:
				return None
			current_index += 1
		return current_node
	

	def read_data(self, index):
		node = self.read_node(index)
		if node:
			return node.data
		else:
			return None
		

	def search(self, value):
		current_index = 0
		current_node = self.first_node
		while(current_node.data != value):
			current_node = current_node.next_node
			if not current_node:
				return None
			current_index += 1
		return current_index


	def delete(self, index):
		if index == 0:
			if self.first_node:
				self.first_node = self.first_node.next_node
		else:
			preceding_node = self.read_node(index - 1)
			if preceding_node and preceding_node.next_node:
				preceding_node.next_node = preceding_node.next_node.next_node

		self.count -= 1


	def append(self, value):
		new_node = SingleSidedNode(value)
		self.last_node.next_node = new_node
		self.last_node = new_node
		self.count += 1 


	def insert(self, index, value):
		new_node = SingleSidedNode(value)

		if index == 0:
			if not self.first_node:
				self.first_node = new_node
			else:
				new_node.next_node = self.first_node
				self.first_node = new_node
		else:
			preceding_node = self.read_node(index-1)
			new_node.next_node = preceding_node.next_node
			preceding_node.next_node = new_node
		
		self.count += 1 


	def update(self, index, value):
		target_node = self.read_node(index)
		if target_node:
			target_node.data = value


	def print(self):
		current_node = self.first_node
		while(current_node):
			print(current_node.data, end=" ")
			current_node = current_node.next_node
		print()


	def detectCycleSet(self):

		visited = set()

		curr = self.first_node
		while curr is not None:
			if curr in visited: return True
			visited.add(curr)
			curr = curr.next

		return False
	

	def detectCycleSlowFast(self):

		slow = self.first_node
		fast = self.first_node
		while slow and fast:
			if not slow.next_node: return False
			slow = slow.next_node
			if not fast.next_node or not fast.next_node.next_node: return False
			fast = fast.next_node.next_node
			if fast == slow: return True

		return False


	def convertArray(a):

		n = len(a)

		if n == 0:
			return None

		link = SinglyLinkedList(a[0])

		if n == 1:
			return link
		
		for i in range(len(a)):
			link.append(a[i])



# doubly linked list


class DoubleSidedNode:

    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.previous_node = None


class DoublyLinkedList:

	def __init__(self, value: int=None):
		self.first_node = None
		self.last_node = None
		self.count = 0
		if value:
			self.append(value)


	def count(self):
		return self.count


	def count_nodes(self):
		current_index = 0
		current_node = self.first_node
		while(current_node):
			current_node = current_node.next_node
			current_index += 1
		return current_index


	def read_data(self, target_index):
		node = self.read_node(target_index)
		if node is not None:
			print("node.data=" + str(node.data))
			return node.data
		else:
			print("node is None")
			return None


	# should be internal only
	def read_node(self, target_index):
		if not self.first_node:
			return None
		current_index = 0
		current_node = self.first_node
		while(current_index < target_index):
			if not current_node.next_node:
				return None
			current_node = current_node.next_node
			current_index += 1
		return current_node


	def update(self, target_index, value):
		target_node = self.read_node(target_index)
		if target_node:
			target_node.data = value


	def search(self, value):
		current_index = 0
		current_node = self.first_node
		while(current_node.data != value):
			current_node = current_node.next_node
			if not current_node:
				return None
			current_index += 1
		return current_index


	def delete(self, delete_index):
		if delete_index == 0:
			if self.first_node:
				node_after_deleted = self.first_node.next_node
				self.first_node = node_after_deleted
				if node_after_deleted:
					node_after_deleted.previous_node = None
		else:
			node_deleted = self.read(delete_index)
			if not node_deleted:
				node_deleted = self.last_node.previous_node
			node_before_deleted = node_deleted.previous_node
			node_after_deleted = node_deleted.next_node
			if node_before_deleted:
				node_before_deleted.next_node = node_after_deleted
			if node_after_deleted:
				node_after_deleted.previous_node = node_before_deleted
		self.count -= 1


	def insert(self, insert_index, value):
		insert_node = DoubleSidedNode(value)
		if insert_index == 0:
			if not self.first_node:
				self.first_node = insert_node
				self.last_node = insert_node
			else:
				self.first_node.previous_node = insert_node
				insert_node.next_node = self.first_node
				insert_node.previous_node = None
				self.first_node = insert_node
		else: 
			node_before_insert_index = self.read_node(insert_index-1)
			if node_before_insert_index:
				node_after_insert = node_before_insert_index.next_node
				insert_node.next_node = node_after_insert
				insert_node.previous_node = node_before_insert_index
				node_before_insert_index.next_node = insert_node
				if node_after_insert:
					node_after_insert.previous_node = insert_node
		self.count += 1


	def append(self, value):
		append_node = DoubleSidedNode(value)
		if not self.first_node:
			self.first_node = append_node
			self.last_node = append_node
		elif not self.last_node:
			self.first_node.next_node = append_node
			append_node.previous_node = self.first_node
			self.last_node = append_node
		else: 
			self.last_node.next_node = append_node
			append_node.previous_node = self.last_node
			self.last_node = append_node
		self.count += 1


	def pop_head(self):
		if not self.first_node: return None
		popped_node = self.first_node
		self.first_node = self.first_node.next_node
		self.count -= 1
		return popped_node.data


	def print(self):
		current_node = self.first_node
		while(current_node):
			print(current_node.data, end=" ")
			current_node = current_node.next_node
		print()
	



class Queue:

	def __init__(self):
		self.data = DoublyLinkedList()

	def Count(self):
		return self.data.count

	def Enqueue(self,value):
		self.data.append(value)

	def Dequeue(self):
		return self.data.pop_head()

	def Read(self):
		if not self.data.first_node: return None
		return self.data.first_node.data


class Dictionary:

	min_size = 8

	def __init__(self, size=8):
		self.size = size
		self.data = [None]*size
		self.keys = []
		self.values = []


	def ResizeUp(self):
		new_size = self.size * 2
		new_data = [None] * new_size
		for i in range(self.size):
			item = self.data[i]
			new_hash_index = hash(item[1]) % new_size
			if new_data[new_hash_index] is None:
				new_data[new_hash_index] = [item]
			else:
				new_data[new_hash_index].append(item)
		self.size = new_size
		self.data = new_data
		

	def ResizeDown(self):
		new_size = self.size // 2
		if new_size < self.min_size:
			return
		new_data = [None] * new_size
		for i in range(self.size):
			item = self.data[i]
			new_hash_index = hash(item[1]) % new_size
			if new_data[new_hash_index] is None:
				new_data[new_hash_index] = [item]
			else:
				new_data[new_hash_index].append(item)
		self.size = new_size
		self.data = new_data


	def ContainsKey(self,key):
		return key in self.keys

	def ContainsValue(self,value):
		return value in self.values


	def Add(self,key,value):
		if len(self.keys) >= self.size * 3 // 2:
			self.ResizeUp()

		hash_index = hash(key) % self.size
		list = self.data[hash_index]
		item = (hash_index,key,value)
		if list is None:
			self.data[hash_index] = [item]
		else:
			self.data[hash_index].append(item)
		if not key in self.keys:
			self.keys.append(key)


	def Delete(self,key):
		if len(self.keys) <= self.size // 4:
			self.ResizeDown()

		hash_index = hash(key) % self.size
		list = self.data[hash_index]
		if list is not None:
			for item in list:
				if item[1] == key:
					list.remove(item)
		if key in self.keys:
			self.keys.remove(key)


	def Update(self,key,value):
		hash_index = hash(key) % self.size
		list = self.data[hash_index]
		if list is not None:
			for i in range(len(list)):
				item = list[i]
				if item[1] == key:
					list[i] = (hash_index,key,value)


	def Read(self,key):
		hash_index = hash(key) % self.size
		list = self.data[hash_index]
		if list is not None:
			for item in list:
				if item[1] == key:
					return item[2]
				


# Question 1 : reverse doubly linked list
# (20 points each)
# 1. Write a function to reverse the elements in a doubly linked list. 
# Do not simply print it out. 
# It must have the references correctly set in reversed order.
# Also, write a print method – this should help with debugging. 
def ReverseDoublyLinkedList(self, list: DoublyLinkedList):
    
    previous = None
    head = list.first_node
    tail = list.last_node
    curr = head
    while curr:
        next = curr.next_node
        curr.next_node = previous
        curr.previous_node = next
        previous = curr
        curr = next
    list.first_node = tail
    list.last_node = head
            


# Question 2 : rotate singly linked list n places to right
# 2. Write a function that accepts a singly linked list and rotates it by n places to the right. 
# If n is negative, rotate it abs(n) places to the left. 
# Ensure the function is efficient and does not convert the linked list to a different data structure. 

# Examples:
# 1->2->3->4->5 (rotate 2) result: 4->5->1->2->3
# 1->2->3->4->5 (rotate -2) result: 3->4->5->1->2


def RotateLinkedList(self, list: SinglyLinkedList, rotate: int):

	# 10 20 30 40 50 rotate 3 (right)
	# preceding == 20
	# 30 40 50 10 20 rotate -3 (left)
	# preceding == 50

	if not list or rotate == 0: return

	n = list.count

	rotate %= n
	if list < 0:
		rotate  += n

	if rotate > 0:
		# 10 20 30 40 50
		preceding_node = list.read_node(list.count-rotate-1)	# for right rotate 3, preceding node should be 20
		if preceding_node: 
			list.last_node.next_node = list.first_node
			list.first_node = preceding_node.next_node
			list.last_node = preceding_node
			preceding_node.next_node = None
	elif rotate < 0:
		# 30 40 50 10 20
		preceding_node = list.read_node(abs(rotate)-1)				# for left rotate 3, preceding node should be 50 
		if preceding_node: 
			# 30 40 50 10 20
			list.last_node.next_node = list.first_node
			list.first_node = preceding_node.next_node
			list.last_node = preceding_node
			preceding_node.next_node = None


def FindNodeAfterFirstNode(self, list: SinglyLinkedList):
		
	if not list.first_node: return None
	
	return list.first_node.next_node


def FindNodePrecedingLastNode(self, list: SinglyLinkedList):
		
	if not list.first_node: return None
	
	curr = list.first_node
	previous = None
	while curr.next_node:
		previous = curr
		curr = curr.next_node

	# sanity check
	if previous.next_node == list.last_node:
		return previous
	else:
		return None


def RotateLastNodeToFirstNode(self, list: SinglyLinkedList):

	if not list: return
	
	if list.count <= 1: return

	preceding_node = FindNodePrecedingLastNode(self, list)
	if preceding_node:
		list.last_node.next_node = list.first_node
		list.first_node = list.last_node
		list.last_node = preceding_node
		preceding_node.next_node = None


def RotateFirstNodeToLastNode(self, list: SinglyLinkedList):

	if not list: return
	
	if list.count <= 1: return

	succeeding_node = list.read(self, 1)
	if succeeding_node:
		list.last_node.next_node = list.first_node
		list.first_node.next_node = None
		list.first_node = succeeding_node


	


# 3. Write a function that takes two linked list and outputs a union of these two linked lists. 
# Make it as efficient as possible. 
# You can assume that each list consists of unique numbers and are not necessarily sorted.
# Also, the order of the output is not significant. 
# Do not use built-in union operators or functions.

# For example:

#  [2, 10, 5, 3, 4] and [4, 7, 8, 3, 11] has a union of [2, 10, 3, 4, 5, 7, 8, 11]


def MergeLinkedLists(self, list_a:SinglyLinkedList, list_b:SinglyLinkedList):

	nums = set()

	node_a = list_a.first_node
	while node_a:
		nums.add(node_a.data)
		preceding_a = node_a
		node_a = node_a.next_node
	node_a = preceding_a

	node_b = list_b.first_node
	preceding_b = node_b
	while node_b: 
		if node_b.data not in nums:
			# effectively delete node_b from list_b and add to tail of list_a
			nums.add(node_b.data)
			node_a.next_node = node_b
			node_a = node_b
			preceding_b.next_node = node_b
			node_b = node_b.next_node
		else:
			preceding_b = node_b
			node_b = node_b.next_node

	return list_a.first_node


# 4. Write the following binary search tree functions to:
# Return the minimum value
# Return the maximum value
# Return the sum of all values
# Return the height (The height of a BST is the number of edges on the longest path from the root node to a leaf node)

# 5. Write a function that accepts a binary tree and verifies whether it fulfills binary search tree conditions.

class BinaryNode:

	def __init__(self,value):
		self.data = value
		self.left:BinaryNode = None
		self.right:BinaryNode = None


class BinarySearchTree:


	def __init__(self, node:BinaryNode=None):
		self.node = node

	def PrintInOrderTraversal(self, node:BinaryNode=None):

		if not node:
			if not self.node: return
			node = self.node
		
		if node.left:
			self.PrintInOrderTraversal(node.left)

		print(node.data, end=" ")

		if node.right:
			self.PrintInOrderTraversal(node.right)


	def Search(self, value, node:BinaryNode=None):
		
		if not node:
			if not self.node: return False
			node = self.node

		if value == node.data: return True

		if value < node.data:
			if not node.left: return False
			return self.Search(value, node.left)

		if value > node.data:
			if not node.right: return False
			return self.Search(value, node.right)

		return False
	

	def Insert(self, value, node:BinaryNode=None):
		
		if not node:
			if not self.node: return False
			node = self.node

		if value == node.data: return True

		if value < node.data:
			if node.left: 
				return self.Insert(value, node.left)
			else:
				node.left = BinaryNode(value)
				return True

		if value > node.data:
			if node.right: 
				return self.Insert(value, node.right)
			else:
				node.right = BinaryNode(value)
				return True

		return False
	

	def Delete(self, value):

		if not self.node: return None

		curr = self.node
		parent = None
		delete = None

		while curr:
			if curr.data == value:
				delete = curr
				break

			parent = curr
			if value < curr.data:
				curr = curr.left
			elif value > curr.data:
				curr = curr.right

		if not delete:
			return None
		
		if delete.left and delete.right:
			self.ReplaceWithSuccessorNode(delete)
		else:	# deleted node has 0 or 1 children
			child = delete.left or delete.right

			if not parent:	# deleting root node
				delete.data = child.data
				delete.left = child.left
				delete.right = child.right
			elif delete == parent.left:
				parent.left = child
			elif delete == parent.right:
				parent.right = child

		return delete


	def ReplaceWithSuccessorNode(node:BinaryNode=None):

		successor = node.right
		if not successor.left:
			node.data = successor.data
			node.right = successor.right
			return
		
		while successor.left:
			parent = successor
			successor = successor.left

		if successor.right:
			parent.left  = successor.right
		else:
			parent.left = None
		
		node = successor.value
		return successor


# 4. Write the following binary search tree functions to:
# Return the minimum value
# Return the maximum value
# Return the sum of all values
# Return the height (The height of a BST is the number of edges on the longest path from the root node to a leaf node)

	def MinValue(self):

		if not self.node: return None

		node = self.node
		while node.left:
			node = node.left

		return node.data


	def MaxValue(self):

		# if not self.node: return None

		node = self.node
		while node.right:
			node = node.right

		return node.data


	def Sum(self, node:BinaryNode=None):

		if not node:
			if not self.node: return None
			node = self.node

		sum = 0

		if node.left:
			sum += self.Sum(node.left)

		sum += node.data

		if node.right:
			sum += self.Sum(node.right)

		return sum


	def Height(self, node:BinaryNode=None):	

		if not node:
			if not self.node: return None
			node = self.node

		if not node.left and not node.right:
			return 0

		path_left = path_right = 0

		if node.left:
			path_left = self.Height(node.left)

		if node.right:
			path_right = self.Height(node.right)

		max_path = max(path_left,path_right)
	
		return max_path + 1
	

# 5. Write a function that accepts a binary tree and verifies whether it fulfills binary search tree conditions.	

	def IsValid(self, node:BinaryNode=None, min_val:int=math.inf, max_val:int=-math.inf):
		if not node:
			if not self.node: return False
			node = self.node

		print('node.data=' + str(node.data))
		print('min_val=' + str(min_val))
		print('max_val=' + str(max_val))

		min_val = min(min_val,node.data)
		max_val = max(max_val,node.data)

		if node.left:
			print('node.left.data=' + str(node.left.data))
			if node.left.data >= node.data or node.left.data >= max_val: return False
			if not self.IsValid(node.left, min_val, max_val): return False

		if node.right:
			print('node.right.data=' + str(node.right.data))
			if node.right.data <= node.data or node.right.data <= min_val: return False 
			if not self.IsValid(node.right, min_val, max_val): return False

		return True
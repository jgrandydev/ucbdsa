import heapq
import math
from collections import Counter, deque, defaultdict

# binary search tree - implemented with nodes

class BinaryNode:

	def __init__(self,value=None):
		self.data = value
		self.left = None
		self.right = None


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
	

# Question 1
# Write a function to get the last item in a complete tree. 
# This is easy to do if the complete tree were implemented using arrays. 
# How would we do this if the tree was implemented using nodes?

	def LastItem(self, node:BinaryNode=None):
		if not node: 
			node = self.node
			if not node: return None

		q = deque()
		q.append(node)
		while q:
			node = q.popleft()
			if node.left:
				q.append(node.left)
			if node.right:
				q.append(node.right)

		print('node.data=' + str(node.data))
		return node.data
	

# heap - implemented with nodes

class HeapNode:

	def __init__(self, data=None):
		self.data = data
		self.left:HeapNode = None
		self.right:HeapNode = None
		self.parent:HeapNode = None
		self.parent_side:str = None


class MinHeap:

	def __init__(self, value=None):
		self.count = 0
		self.top = None
		if value:
			self.top = HeapNode(value)
			self.count += 1


	def count(self):
		return self.count
	

	def count_nodes(self, curr=None):
		if not curr:
			curr = self.top
		count = 1
		if curr.left:
			count += self.count_nodes(self, curr.left)
		if curr.right:
			count += self.count_nodes(self, curr.right) 
		return count
	

	def read_top(self):
		if self.top:
			return self.top.data
		else:
			return None
		

	def remove(self):
		if not self.top: return None
		top = self.top.data
		self.top.data = self.delete_last_node(self.top)
		self.bubble_down(self.top)
		count -= 1
		return top 
	

	def insert(self, value):
		new_node = HeapNode(value)
		if not self.top:
			self.top = new_node
		else:
			last_node= self.find_last_node(self.top)
			if last_node.parent_side == 'left':
				last_node.parent.right = new_node
			elif last_node.parent_side == 'right':
				if not last_node.parent.parent.right:
					last_node.parent.parent.right = new_node 
				else:
					last_node.parent.parent.right.left = new_node
			self.bubble_up(new_node)


	def find_last_node(self, curr:HeapNode):
		if not curr.left and not curr.right:
			return curr
		if curr.right:
			return self.find_last_node(curr.right)
		if curr.left:
			return self.find_last_node(curr.left)


	def delete_last_node(self, curr:HeapNode):
		last_node = self.find_last_node(curr)
		if last_node.parent_side == 'left':
			last_node.parent.left = None
		elif last_node.parent_side == 'right':
			last_node.parent.right = None
		return last_node.data
	

	def bubble_down(self, curr:HeapNode):

		data = curr.data

		if curr.left and curr.right:
			if curr.left.data < curr.right.data and curr.left.data < curr.data:
				curr.data,curr.left.data = curr.left.data,curr.data
				self.bubble_down(curr.left)
			elif curr.right.data < curr.left.data and curr.right.data < curr.data:
				curr.data,curr.right.data = curr.right.data,curr.data
				self.bubble_down(curr.right)
		elif curr.left and curr.left.data < curr.data:	
				curr.data,curr.left.data = curr.left.data,curr.data
				self.bubble_down(curr.left)
		elif curr.right and curr.right.data < curr.data:
				curr.data,curr.right.data = curr.right.data,curr.data
				self.bubble_down(curr.right)

	
	def bubble_up(self, curr:HeapNode):

		if curr.parent.data < curr.data:
			curr.data,curr.parent.data = curr.parent.data,curr.data
			self.bubble_up(curr.parent)


	def print(self, node:HeapNode=None):
		print(node.data)
		if node.left:
			print(node.left.data, end=" ")
		elif node.right:
			print(node.right.data, end=" ")


class MaxHeap:

	def __init__(self, value=None):
		self.count = 0
		self.top = None
		if value:
			self.top = HeapNode(value)
			self.count += 1


	def count(self):
		return self.count
	

	def count_nodes(self, curr=None):
		if not curr:
			curr = self.top
		count = 1
		if curr.left:
			count += self.count_nodes(self, curr.left)
		if curr.right:
			count += self.count_nodes(self, curr.right) 
		return count
	

	def read(self):
		if self.top:
			return self.top.data
		else:
			return None
		

	def remove(self):
		if not self.top: return None
		top = self.top.data
		self.top.data = self.delete_last_node(self.top)
		self.bubble_down(self.top)
		self.count -= 1
		return top 
	

	def insert(self, value):
		new_node = HeapNode(value)
		if not self.top:
			self.top = new_node
		else:
			last_node= self.find_last_node(self.top)
			if last_node.parent_side == 'left':
				new_node.parent = last_node.parent
				new_node.parent_side = 'right'
				last_node.parent.right = new_node
			elif last_node.parent_side == 'right':
				if not last_node.parent.parent.right:
					new_node.parent = last_node.parent.parent
					new_node.parent_side = 'right'
					last_node.parent.parent.right = new_node 
				else:
					new_node.parent = last_node.parent.parent.right
					new_node.parent_side = 'left'
					last_node.parent.parent.right.left = new_node
			self.bubble_up(new_node)
			self.count += 1


	def find_last_node(self, curr:HeapNode):
		if not curr.left and not curr.right:
			return curr
		if curr.right:
			return self.find_last_node(curr.right)
		if curr.left:
			return self.find_last_node(curr.left)


	def delete_last_node(self, curr:HeapNode):
		last_node = self.find_last_node(curr)
		if last_node.parent_side == 'left':
			last_node.parent.left = None
		elif last_node.parent_side == 'right':
			last_node.parent.right = None
		return last_node.data
	

	def bubble_down(self, curr:HeapNode):

		data = curr.data

		if curr.left and curr.right:
			if curr.left.data > curr.right.data and curr.left.data > curr.data:
				curr.data,curr.left.data = curr.left.data,curr.data
				self.bubble_down(curr.left)
			elif curr.right.data > curr.left.data and curr.right.data > curr.data:
				curr.data,curr.right.data = curr.right.data,curr.data
				self.bubble_down(curr.right)
		elif curr.left and curr.left.data > curr.data:	
				curr.data,curr.left.data = curr.left.data,curr.data
				self.bubble_down(curr.left)
		elif curr.right and curr.right.data > curr.data:
				curr.data,curr.right.data = curr.right.data,curr.data
				self.bubble_down(curr.right)

	
	def bubble_up(self, curr:HeapNode):

		if curr.parent and curr.parent.data < curr.data:
			curr.data,curr.parent.data = curr.parent.data,curr.data
			self.bubble_up(curr.parent)


	def print(self, node:HeapNode=None):
		print(node.data)
		if node.left:
			print(node.left.data, end=" ")
		elif node.right:
			print(node.right.data, end=" ")



# min heap - implemented using array

class MinHeapArray:

	def __init__(self, value=None):
		self.array = []
		self.insert(value)

	def final_index(self):
		return len(self.array)-1

	def parent_index(index):
		if index % 2 == 0:	# right index
			return index - 2
		else:				# left index
			return index - 1

	def left_child_index(index):
		return 2 * index + 1

	def right_child_index(index):
		return 2 * index + 2

	def read(self):
		return self.array[0]

	def remove(self):
		val = self.array[0]
		final_index = self.final_index()
		self.array[0] = self.array[final_index]
		del self.array[final_index]
		self.bubble_down(0)
		return val

	def insert(self, value):
		self.array.append(value)
		self.bubble_up(self.final_index())
	
	def bubble_up(self, index):
		while index > 0:
			parent_index = self.parent_index(index)
			if self.array[index] < self.array[parent_index]:
				self.array[index],self.array[parent_index] = self.array[parent_index],self.array[index]
				index = parent_index
			else:
				break

	def bubble_down(self, index):
		final_index = self.final_index()
		while index < final_index:
			left_index = self.left_child_index(index)
			right_index = self.right_child_index(index)

			comparison_index = None	# want the index with the greater value
			if left_index > final_index and right_index <= final_index:
				comparison_index = right_index
			if right_index > final_index and left_index <= final_index:
				comparison_index = left_index
			elif left_index <= final_index and right_index <= final_index:
				if self.array[left_index] <= self.array[right_index]:
					comparison_index = left_index
				else:
					comparison_index = right_index
			
			if comparison_index:
				if self.array[comparison_index ] < self.array[index]:
					self.array[comparison_index ] , self.array[index] = self.array[index] , self.array[comparison_index] 
				else:
					break


	def print(self):
		for e in self.array:
			print(e, end=" ")
		print()


# max heap - implemented using array

class MaxHeapArray:

	def __init__(self):
		self.array = []

	def count(self):
		return len(self.array)

	def final_index(self):
		return len(self.array)-1

	def parent_index(self,index):
		return (index-1) // 2

	def left_child_index(self,index):
		return 2 * index + 1

	def right_child_index(self,index):
		return 2 * index + 2

	def read(self):
		return self.array[0]

	def insert(self, value):
		self.array.append(value)
		if len(self.array) > 1:
			self.bubble_up(self.final_index())
	
	def remove(self):
		if self.count() > 0:
			val = self.array[0]
			final_index = self.final_index()
			self.array[0] = self.array[final_index]
			del self.array[final_index]
			self.bubble_down(0)
			return val

	def bubble_up(self, index):
		while index > 0:
			parent_index = self.parent_index(index)
			if self.array[index] > self.array[parent_index]:
				self.array[index],self.array[parent_index] = self.array[parent_index],self.array[index]
				index = parent_index
			else:
				break

	def bubble_down(self, index):
		final_index = self.final_index()
		while index < final_index:
			left_index = self.left_child_index(index)
			right_index = self.right_child_index(index)

			if (left_index > final_index or not self.array[left_index]):
				break

			comparison_index = None	# want the index with the greater value
			if left_index > final_index and right_index <= final_index:
				comparison_index = right_index
			if right_index > final_index and left_index <= final_index:
				comparison_index = left_index
			elif left_index <= final_index and right_index <= final_index:
				if self.array[left_index] >= self.array[right_index]:
					comparison_index = left_index
				else:
					comparison_index = right_index
			
			if comparison_index:
				if self.array[comparison_index ] > self.array[index]:
					self.array[comparison_index ] , self.array[index] = self.array[index] , self.array[comparison_index] 
					index = comparison_index
				else:
					break


	def print(self):
		for e in self.array:
			print(e, end=" ")
		print()



				
# Question 2
# Write a function that accepts a string and returns an array of the characters in the string sorted by frequency 
# (from most frequent to least frequent).
# You must use a heap to sort the characters. You can use the heap in the dsa package, Python's heapq package or write your own. 
# Example: 
# The input
#  "abracadabra"
# should return:
# ['a', 'b', 'r', 'c', 'd']
# Note: characters that have the same frequency can appear in any order


# def CharFrequencyHeap(s):
# 	counts = Counter(s)
# 	heap = MaxHeap()
# 	for c in counts.keys():
# 		heap.insert((counts[c],c))
# 	ans = []
# 	while heap:
# 		ans.append(heap.pop())
# 	return ans


def CharFrequencyHeapArray(s):
	counts = defaultdict(int)
	for c in s:
		counts[c] += 1
	heap = MaxHeapArray()
	for c in counts:
		heap.insert((counts[c],c))
	ans = []
	while heap.count() > 0:
		item = heap.remove()
		ans.append(item[1])
	return ans


def CharFrequencyHeapq(s):
	counts = defaultdict(int)
	for c in s:
		counts[c] += 1
	heap = []
	for c in counts:
		heapq.heappush(heap,(-counts[c],c))
	ans = []
	while heap:
		count,c = heapq.heappop(heap)
		ans.append(c)
	return ans


# Question 3
# Write a function that accepts an array of words, stores them in a trie and returns the longest common prefix. 
# Write it so that it performs efficiently.
# For example, given the array

# words = ["apple", "appetite", "apparatus", "appliance"]
# The function should return

# "app"


class TrieNode():

	def __init__(self,value:str=None):
		self.data:str = value
		self.children:list[TrieNode] = []
		self.parent:TrieNode = None


class Trie():

	def __init__(self, words=None):

		self.root:TrieNode = TrieNode()
		self.count:int = 0

		if words:
			self.BuildTrie(words)


	def BuildTrie(self, words: list[str]):
		for word in words:
			self.AddWord(self.root,word)


	def AddWord(self, root:TrieNode, word:str):
		if not root:
			root = self.root

		curr = None
		for child in root.children:
			if child.data == word[0]:
				curr = child
				break
		if not curr:
			curr = TrieNode(word[0])
			root.children.append(curr)
		if len(word) > 1:
			self.AddWord(curr, word[1:])
		else:
			curr.children.append(TrieNode('*'))
		self.count += 1


	def LongestCommonPrefix(self):
		prefix = ''
		children = self.root.children
		while len(children) == 1:
			prefix += children[0].data
			children = children[0].children
		return prefix
	

	def ShortestUniquePrefixes(self):
		children = self.root.children
		prefixes = []
		for child in children:
			prefixes += self.ShortestUniquePrefixesContinuation('',child)
		return prefixes


	def ShortestUniquePrefixesContinuation(self, prefix:str='', node:TrieNode=None):
		prefixes = []
		if node.data == '*':
			prefixes.append(prefix[0])
		else:
			if len(node.children) == 1:
				prefixes += self.ShortestUniquePrefixesContinuation(prefix + node.data, node.children[0])
			elif len(node.children) > 1:
				prefix += node.data
				for child in node.children:	
					if child.data == '*':
						prefixes.append(prefix)
					else:		
						prefixes.append(prefix + child.data)
		return prefixes
	

# Question 5
# Write a search function or method for a Trie data structure. 
# The search word may contain the dot character '.' to represent any single letter.
# 15 points maximum if the function returns True or False for each search query
# (more challenging) 20 points maximum if the function returns an array of words that match the wildcard search
# Examples:i
# Assume that the Trie has the following words:
# apple, apply, application, banana
# trie.search("apple")  # Returns: True
# trie.search("app")    # Returns: False
# trie.search("appl.")  # Returns: True
# trie.search("ap.le")  # Returns: True
# trie.search_all("app.e")  # Returns: ["apple"]
# trie.search_all("ap.l.")  # Returns: ["apple", "apply"]


	def Search(self, search):
		children = self.root.children
		matches = []
		for child in children:
			matches += self.SearchContinuation(search, child, '')
		return matches


	def SearchContinuation(self, search:str='', node:TrieNode=None, partial:str=''):
		matches = []
		if len(search) == 0: 
			if node.data == '*': matches.append(partial)
		else:
			if search[0] == '.' or node.data == search[0]:
				for child in node.children:	
					matches += self.SearchContinuation(search[1:], child, partial + node.data)
		return matches

	
# Question 3
# Write a function that accepts an array of words, stores them in a trie and returns the longest common prefix. 
# Write it so that it performs efficiently.
# For example, given the array
# words = ["apple", "appetite", "apparatus", "appliance"]
# The function should return
# "app"

def LongestCommonPrefixForWords(words:list[str]):
	trie = Trie(words)
	return trie.LongestCommonPrefix()


# Question 4
# Write a function that accepts an array of words and then returns the shortest unique prefix of each word. 
# For example:
# words = ['apple', 'banana', 'cherry', 'cranberry', 'grape', 'grapefruit'] 
# # 'apple' returns 'a'
# # 'banana' returns 'b'
# # 'cherry' returns 'ch'
# # 'cranberry' returns 'cr'
# # 'grape' returns 'grape'
# # 'grapefruit' returns 'grapef'
# # returns:
# ['a', 'b', 'ch', 'cr', 'grape', 'grapef']

def ShortestUniquePrefixesForWords(words:list[str]):
	trie = Trie(words)
	return trie.ShortestUniquePrefixes()


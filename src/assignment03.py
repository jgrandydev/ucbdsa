# Describe the worst case data and the best case data for each of the following sorting algorithms. 
# Also, include the big O notation for each case.


# Bubble Sort
# worst case : goal is sort ascending but data is pre-sorted descending, comparisons always swap, every element bubbles max distance
# 			   N passes * (N comparisons + N swaps), N * 2 * N = O(N^2)
# best case : goal is sort ascending and data is pre-sorted ascending, comparisons never swap
#             single pass, each element one comparison, N * 1 = O(N)


# Selection Sort
# worst case : goal is sort ascending but data is pre-sorted descending, comparisons always select next, plus final swap
#              N passes of avg N/2 comparisons = N * N/2 = N^2/2 = O(N^2)
# best case : goal is sort ascending and data is pre-sorted ascending, comparisons never select next, no swaps
# 			  N passes of avg N/2 comparisons = N * N/2 = N^2/2 = O(N^2)


# Insertion Sort
# worst case : goal is sort ascending but data is descending, each successive element must bubble down to bottom
#              N passes of avg N/2 comparisons + avg N/2 swaps = N * (N/2 + N/2)= O(N^2)
# best case : goal is sort ascending and data is pre-sorted ascending, comparisons never cause a swap
# 			  N passes of avg N/2 comparisons = N^2/2 = O(N^2)


# Merge Sort
# worst case : goal is sort ascending but data is pre-sorted descending, 
# 			   every partion comparison results in a swap-merge  
#              -> logN levels , total N swaps-merges per level = 2 * N * LogN = O(NLogN)
# best case : goal is sort ascending and data is pre-sorted ascending, full partitions, 
# 			  every partition comparison results in merge only, no swap
# 			  -> LogN levels, each level = N*LogN = O(NLogN)


# Quicksort
# worst case : 	if algo chooses pivot as first or last element in each partition, and array is already sorted or nearly sorted,
# 			   	then nearly-full partition ( minus the pivot only ) is recursively sorted , so N passes of N elements
#              	-> N passes of avg N comparisons = N*N = O(N^2)
# best case :   if algo chooses middle or near-middle element in each partition, then log n levels will each sort n elements,
# 			  	log N levels of ~N comparisons = logN*N = O(nlogn)



class Solution:


	# Question 2 implement insertion sort iterative
	# NOTE : for initial call n should be set to len(a) - 1
	def insertionSortIterative(a):
		i = 1
		while i < len(a):
			val = a[i]
			j = i
			while j > 0 and a[j-1] > val:
				a[j] = a[j-1]
				j -= 1
			a[j] = val
			i += 1


 	# Question 2 implement insertion sort recursive
	# NOTE : for initial call n should be set to len(a) - 1
	def insertionSortRecursive(a,n):
		if n <= 0: 
			return
		Solution.insertionSortRecursive(a,n-1)
		val = a[n]
		j = n - 1
		while j >= 0 and a[j] > val:
			a[j+1] = a[j]
			j -= 1
		a[j+1] = val	# insert val into correct slot


	# Question 3 implement find missing numbers
	def findMissingNumbers(a):
		n = len(a)
		numbers = set()
		for i in range(n):
			numbers.add(a[i])
		missing = []
		for i in range(n):
			if i not in numbers:
				missing.append(i)
		return missing


	# Question 4 implement longest consecutive subsequence
	def findLongestConsecutiveSubsequence(a):
		n = len(a)
		numbers = set()
		for i in range(n):
			numbers.add(a[i])
		longest_subarray = []
		for i in range(n):
			val = a[i]
			sub = []
			while val in numbers:
				sub.append(val)
				val += 1
			if len(sub) > len(longest_subarray):
				longest_subarray = sub
		return longest_subarray
		

# 5. Write a function that given an array of integers and a target value, 
# returns the length of the longest subarray with a sum equal to the target value. 
# Write the function with O(n) efficiency for full credit.

# Note: while the sliding window technique is acceptable as a solution, try solving this using a hash table.
 
# For example:
# Given an array [3, 1, -1, 2, -1, 5, -2, 3] and a target value of 3, the longest subarray length is 5 ([-1, 2, -1, 5, -2])


	# Question 5 implement longest subarray with sum = target (sliding window)
	# time complexity = N * N/2 (avg) = N^2/2 = O(N^2) -- this is not good , we must do better
	def findLongestSubarraySumTarget_SlidingWindow(a, target):
		
		n = len(a)
		i = 0
		j = 0
		sum = 0
		longest = 0
		for i in range(n):
			sum = a[i]
			if sum == target:
				longest = max(longest, j-i+1)
			for j in range(i+1,n):
				sum += a[j]
				if sum == target:
					longest = max(longest, j-i+1)
		return longest
	
			
	# Question 5 implement longest subarray with sum = target (hashtable)
	# total sum - prefix sum = target  
	# prefix sum = total sum - target
	# time complexity = O(N)
	def findLongestSubarraySumTarget_PrefixSum(a, target):

		prefix_sum = {}
		prefix_sum[0] = -1
		longest = 0
		sum = 0
		for i,val in enumerate(a):
			sum += val
			remainder = sum - target
			if remainder in prefix_sum:
				longest = max(i - prefix_sum[remainder], longest)
			if sum not in prefix_sum:
				prefix_sum[sum] = i
		return longest



class LinkedList:

	class Node:

		def __init__(self, data):
			self.data = data
			self.next_node = None


	def __init__(self, value):
		node = LinkedList.Node(value)
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


	def read_data(self, index):
		node = self.read_node(index)
		if node:
			return node.data
		else:
			return None


	def read_node(self, target_index):
		current_index = 0
		current_node = self.first_node
		while(current_index < target_index):
			current_node = current_node.next_node
			if not current_node:
				return None
			current_index += 1
		return current_node


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
		new_node = LinkedList.Node(value)
		self.last_node.next_node = new_node
		self.last_node = new_node
		self.count += 1 


	def insert(self, index, value):
		new_node = LinkedList.Node(value)

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

		link = LinkedList(a[0])

		if n == 1:
			return link
		
		for i in range(len(a)):
			link.append(a[i])


class DoublyLinkedList:

	class Node:

		def __init__(self, data):
			self.data = data
			self.next_node = None
			self.previous_node = None


	def __init__(self, first_node:Node = None, last_node:Node = None):
		self.first_node = first_node
		self.last_node = last_node
		if not self.first_node:
			self.first_node = self.last_node
		if not self.last_node:
			self.last_node = self.first_node
		

	def count(self):
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


	def insert(self, insert_index, value):
		insert_node = DoublyLinkedList.Node(value)
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


	def append(self, value):
		append_node = DoublyLinkedList.Node(value)
		if not self.first_node:
			self.first_node = append_node
			self.last_node = append_node
		elif not self.last_node :
			self.first_node.next_node = append_node
			append_node.previous_node = self.first_node
			self.last_node = append_node
		else: 
			self.last_node.next_node = append_node
			append_node.previous_node = self.last_node
			self.last_node = append_node


	def pop_head(self):
		if not self.first_node: return None
		popped_node = self.first_node
		self.first_node = self.first_node.next_node
		return popped_node.data


class Queue:

	def __init__(self):
		self.data = DoublyLinkedList()

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

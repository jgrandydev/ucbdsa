from typing import Any, List

# binary search tree - implemented with nodes

class ListNode:

	def __init__(self,value=None):
		self.data = value
		self.next = None


class Vertice:

	def __init__(self,key,value=None):
		self.key = key
		self.data = value
		self.edges:List[Edge] = []


class Edge:

	def __init__(self,vertice1=None,vertice2=None,value=None,):
		self.vertice1 = vertice1
		self.vertice2 = vertice2
		self.data = value


class DirectedEdge:

	def __init__(self,head=None,tail=None,value=None,):
		self.head:Vertice = head
		self.tail:Vertice = tail
		self.data = value


class Graph:

	def __init__(self, vertices:List[Vertice]=None):
		self.vertices:List[Vertice] = vertices
		self.adjacencylist = {}
		self.BuildAdjacencyListArray()
		self.BuildAdjacencyMatrix()


	def PrintAdjacencyMatrix(self):
		n = len(self.vertices)
		for i in range(n):
			print()
			for j in range(n):
				print(self.adjacencymatrix[i][j], end=' ')


	def BuildAdjacencyMatrix(self):
		n = len(self.vertices)
		self.adjacencymatrix = [[0 for _ in range(n)] for _ in range(n)]
		for i in range(n):
			vertice = self.vertices[i]
			self.adjacencymatrix[i][i] = 0	# acyclic because not using directed edges
			for edge in vertice.edges:
				connectedkey = edge.vertice2.key if edge.vertice1 == vertice else edge.vertice1.key
				for j in range(n):
					if connectedkey == self.vertices[j].key: break
				self.adjacencymatrix[i][j] = 1
				self.adjacencymatrix[j][i] = 1


	def BuildAdjacencyListArray(self):
		self.adjacencylist = {}
		for vertice in self.vertices:
			others = []
			for edge in vertice.edges:
				other:Vertice = edge.vertice2 if edge.vertice1 == vertice else edge.vertice1
				others.append(other.key)
			self.adjacencylist[vertice.key] = others


	def BuildAdjacencyListLinkedList(self):
		if not self.vertices or len(self.vertices) == 0: return
		self.adjacencylist = []
		for vertice in self.vertices:
			root = None
			curr = None
			for edge in vertice.edges:
				other = edge.vertice2 if edge.vertice1 == vertice else edge.vertice1
				node = ListNode(other)
				if not root and not curr:
					root = node
					curr = node
				else:
					curr.next = node
					curr = node
			self.adjacencylist[vertice] = root


	def dfs(self, value, curr:Vertice=None):
		if len(self.vertices) == 0: return None
		if not curr: curr = self.vertices[0]
		path = [curr.data]
		if curr.data == value: return path


	def bfs_adjacencylist(self, start:Vertice, target:Vertice, path:List[Any]=[]):

		def recurse(target, connections:List[Any], path:List[Any]):
			for key in connections:
				if key not in visited:
					visited.add(key)
					path.append(key)
					if key == target: return True
					next_connections = self.adjacencylist[key]
					if recurse(target,next_connections,path): return True
					path.remove(key)
			return False
				

		if not self.vertices: return False
		if len(self.vertices) == 0: return False
		if not self.adjacencylist: return False
		if not start in self.adjacencylist: return False
		visited = set()
		visited.add(start) 
		path.append(start)
		if target == start: return True
		connections = self.adjacencylist[start]
		return recurse(target, connections, path)
	

	def bfs_adjacencymatrix(self, start:Vertice, target:Vertice, path:List[Any]):

		def recurse(i, target, path:List[Any]):
			for j in range(n):
				if self.adjacencymatrix[i][j] == 1:
					next = self.vertices[j]
					if next.key not in visited:
						visited.add(next.key)
						path.append(next.key)
						if next.key == target: return True
						if recurse(j,target,path): return True
						path.remove(next.key)
			return False

		if not self.vertices: return False
		n = len(self.vertices)
		if n == 0: return False
		if not self.adjacencymatrix: return False
		visited = set()
		visited.add(start) 
		path.append(start)
		for i in range(n):
			if self.vertices[i].key == start: 
				break
		return recurse(i, target, path)  


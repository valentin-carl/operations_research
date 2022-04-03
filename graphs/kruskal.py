import numpy as np

class Id:
	def __init__(self):
		self.id = 0

	def get_id(self) -> int:
		res = self.id
		self.id += 1
		return res

node_id = Id()

class Node:
	def __init__(self):
		self.id = chr(node_id.get_id()+97)
		self.edges = []

class Edge:
	def __init__(self, n1: Node, n2: Node, weight = 0):
		self.n1 = n1
		self.n2 = n2
		self.weight = weight
		self.n1.edges.append(self)

class Graph:
	def __init__(self, nodes: list[Node], edges: list[Edge]):
		self.nodes = nodes
		self.edges = edges

	def MST(self) -> list[Edge]:
		# list of sorted edges (using insertion sort)
		sorted_edges = []
		for edge in self.edges:
			index = 0
			while index < len(sorted_edges) and edge.weight > sorted_edges[index].weight:
				index += 1
			sorted_edges.insert(index, edge)

		mst = [] # list of edges that will make up the MST
		nodes = set() # set of nodes in MST
		while len(nodes) < len(self.nodes):
			potential_edge = sorted_edges[0]
			
			# check if adding that edge would create a circle
			temp = mst[:]
			temp.append(potential_edge)
			creates_circle = self.is_cyclic(potential_edge.n1, set())	
			# add edge to MST
			if not creates_circle:
				mst.append(potential_edge)
				nodes.add(potential_edge.n1)
				nodes.add(potential_edge.n2)

		return mst

	def is_cyclic(self, current: Node, seen: set[Node]) -> bool:
		
		# end recursion
		if current in seen:
			return True

		# change values
		seen.add(current)
	
		# next calls
		for edge in current.edges:
			if self.is_cyclic(edge.n2, seen):
				return True	

		# if reached => end of DFS and no circle found
		return False

	def print(self):
		print(self.nodes)
		print(self.edges)

	def generate(matrix):
		"""
		the input matrix should have the following form:
		   a   b   c   d
		a  0   3   0   0
		b -3   0   5  -2
		c  0  -5   0   4
		d  0   2  -4   0,
		with 0 meaning no edge exists between nodes i and j,
		a_{ij} > 0 meaning an edge exists from i to j with weight abs(a_{ij}),
		and a_{ij} < 0 meaning an edge exists from j to i with weight abs(a_{ij})
		"""
		
		# create nodes list
		nodes = []
		for i in range(0, matrix.shape[0]):
			nodes.append(Node())
		
		# create edges list
		edges = []
		for i in range(matrix.shape[0]):
			for j in range(len(matrix[i])):
				if matrix[i][j] <= 0:
					pass
				else:
					e = Edge(nodes[i], nodes[j], matrix[i][j])
					edges.append(e)

		g = Graph(nodes, edges)
		return g

matrix = np.array([[0,5,1,1,0,0,0],
                   [5,0,0,2,1,0,0],
                   [1,0,0,2,0,3,0],
                   [1,2,2,0,3,2,4],
                   [0,1,0,3,0,0,4],
                   [0,0,3,2,0,0,1],
                   [0,0,0,4,4,1,0]])
g = Graph.generate(matrix)
print(g.MST())

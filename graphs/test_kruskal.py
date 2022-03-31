import pytest
import kruskal as k
import numpy as np

def test_node_id():
	for i in range(26):
		n = k.Node()
		print(n.id)
		assert n.id == chr(97+i)

def test_edge():
	n1 = k.Node()
	n2 = k.Node()
	edge = k.Edge(n1, n2, 3.14)
	assert edge.n1 == n1
	assert edge.n2 == n2
	assert edge.weight == 3.14

def test_generate():
	matrix = np.array([[0, 3, 0, 0],
			  [-3, 0, 5, -2],
			  [0, -5, 0, 4],
			  [0, 2, -4, 0]])
	g = k.Graph.generate(matrix)
	assert len(g.nodes) == matrix.shape[0]
	assert len(g.nodes) == 4
	assert len(g.edges) == 4

def test_circle():
	matrix = np.array(
		[[0, 1, -1],
		[-1, 0, 1 ],
		[1, -1 , 0]])
	g = k.Graph.generate(matrix)
	assert g.is_cyclic(g.nodes[0], set()) == True

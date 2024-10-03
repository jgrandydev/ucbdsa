import unittest

from assignment06 import Graph
from assignment06 import Vertice
from assignment06 import Edge


class Test_TestAssignment06(unittest.TestCase):

    def testGraphBfs(self):

        #                 100
        #     50                      150
        # 25      75              125     175          

        v100 = Vertice(100)
        v50 = Vertice(50)
        v150 = Vertice(150)
        v25 = Vertice(25)
        v75 = Vertice(75)
        v125 = Vertice(125)
        v175 = Vertice(175)
        e100_50 = Edge(v100,v50)
        e100_150 = Edge(v100,v150)
        e50_25 = Edge(v50,v25)
        e50_75 = Edge(v50,v75)
        e150_125 = Edge(v150,v125)
        e150_175 = Edge(v150,v175)
        v100.edges.append(e100_50)
        v100.edges.append(e100_150)
        v50.edges.append(e50_25)
        v50.edges.append(e50_75)
        v150.edges.append(e150_125)
        v150.edges.append(e150_175)

        vertices = []
        vertices.append(v100)
        vertices.append(v50)
        vertices.append(v150)
        vertices.append(v25)
        vertices.append(v75)
        vertices.append(v125)
        vertices.append(v175)

        graph = Graph(vertices)

        graph.PrintAdjacencyMatrix()

        path = []
        self.assertEqual(graph.bfs_adjacencylist(100,175,path), True)
        self.assertEqual(path, [100,150,175])


        path = []
        self.assertEqual(graph.bfs_adjacencymatrix(100,175,path), True)
        self.assertEqual(path, [100,150,175])








     
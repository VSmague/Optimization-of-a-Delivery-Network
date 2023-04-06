import sys 
sys.path.append("delivery_network")

from graph import Graph, graph_from_file

import unittest   # The test framework

class Test_Dist(unittest.TestCase):
        
    def test_network7(self):
        g = graph_from_file("input/network.04.in")
        self.assertEqual(g.graph[1][0][2], 6)
        self.assertEqual(g.graph[1][1][2], 89)
        g1=graph_from_file("input/network.01.in")
        self.assertEqual(g1.graph[1][0][2], 1)
        
"""ca renvoie pas les chemins sous la bonne forme"""
if __name__ == '__main__':
    unittest.main()

# This will work if ran from the root folder.
import sys 
sys.path.append("delivery_network")

from graph import Graph, graph_from_file

import unittest   # The test framework

class Test_Min(unittest.TestCase):
        
    def test_network2(self):
        g = graph_from_file("input/network.02.in")
        self.assertEqual(g.get_path_with_power(1, 2, 11), [1, 2])

    def test_network3(self):
        g = graph_from_file("input/network.05.in")
        self.assertEqual(g.get_path_with_power(1, 3, 11), [1, 3])
        
"""ca renvoie pas les chemins sous la bonne forme"""
if __name__ == '__main__':
    unittest.main()
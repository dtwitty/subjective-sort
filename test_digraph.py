from unittest import TestCase

from digraph import DiGraph

__author__ = 'dominick'


class TestDiGraph(TestCase):
    def test_add_node(self):
        G = DiGraph()

        G.add_node(1)
        self.assertTrue(1 in G)
        self.assertFalse(2 in G)

        G.add_node(2)
        self.assertTrue(1 in G)
        self.assertTrue(2 in G)

    def test_add_edge(self):
        G = DiGraph()

        G.add_node(1)
        G.add_node(2)
        self.assertFalse(G.contains_edge(1, 2))
        self.assertFalse(G.contains_edge(2, 1))

        G.add_edge(1, 2)
        self.assertTrue(G.contains_edge(1, 2))
        self.assertFalse(G.contains_edge(2, 1))

        G.add_edge(2, 1)
        self.assertTrue(G.contains_edge(1, 2))
        self.assertTrue(G.contains_edge(2, 1))

    def test_remove_edge(self):
        G = DiGraph()

        for a in range(1, 4):
            G.add_node(a)

        for a in range(1, 4):
            for b in range(1, 4):
                if a != b:
                    G.add_edge(a, b)

        for a in range(1, 4):
            for b in range(1, 4):
                if a != b:
                    self.assertTrue(G.contains_edge(a, b))

        G.remove_edge(1, 3)
        self.assertTrue(G.contains_edge(3, 1))
        self.assertFalse(G.contains_edge(1, 3))

        G.remove_edge(3, 1)
        self.assertFalse(G.contains_edge(3, 1))
        self.assertFalse(G.contains_edge(1, 3))

        for a in range(1, 4):
            for b in range(1, 4):
                if (a, b) != (1, 3) and (a, b) != (3, 1) and a != b:
                    self.assertTrue(G.contains_edge(a, b))

    def test_remove_node(self):
        G = DiGraph()
        for a in range(1, 4):
            G.add_node(a)

        for a in range(1, 4):
            for b in range(1, 4):
                if a != b:
                    G.add_edge(a, b)

        G.remove_node(3)
        self.assertFalse(3 in G)
        for a in range(1, 3):
            for b in range(1, 3):
                if a != b:
                    self.assertTrue(G.contains_edge(a, b))

        for a in G:
            node = G[a]
            self.assertFalse(3 in node.inward_edges())
            self.assertFalse(3 in node.outward_edges())


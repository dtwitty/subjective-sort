__author__ = 'dominick'

from unittest import TestCase
from copy import deepcopy

from algos import topological_sort, remove_cycles, CycleDetectedException

from digraph import DiGraph


# An example DAG, as found at
# http://en.wikipedia.org/wiki/Topological_sorting
DAG_ADJ = {
    7: [11, 8],
    5: [11],
    3: [8, 10],
    11: [2, 9, 10],
    8: [9],
    2: [],
    9: [],
    10: []
}


def generate_digraph(adj_list: dict):
    """
    :return: A DiGraph formed from the given adjacency list
    """
    G = DiGraph()
    for n in adj_list:
        G.add_node(n)
    for n in adj_list:
        for m in adj_list[n]:
            G.add_edge(n, m)
    return G


def is_topological_sort(G: DiGraph, L: list):
    """
    :return: Whether L is a topological sort of G.
    """
    G = deepcopy(G)
    for n in L:
        if G[n].in_degree() > 0:
            return False
        G.remove_node(n)

    return len(G) == 0


def has_cycle(G: DiGraph):
    """
    :return: Whether G contains a cycle
    """
    try:
        L = topological_sort(G)
        return False
    except CycleDetectedException:
        return True


class TestAlgos(TestCase):
    def test_topological_sort_dag(self):
        G = generate_digraph(DAG_ADJ)
        L = topological_sort(G)
        self.assertTrue(is_topological_sort(G, L))

    def test_topological_sort_cycle(self):
        G = generate_digraph(DAG_ADJ)
        self.assertFalse(has_cycle(G))

        # add an edge to create a cycle
        G.add_edge(10, 7)
        self.assertTrue(has_cycle(G))

    def test_remove_cycles(self):
        G = generate_digraph(DAG_ADJ)
        # add an edges to create cycles
        G.add_edge(10, 7)
        G.add_edge(2, 3)
        G.add_edge(2, 5)
        self.assertTrue(has_cycle(G))

        remove_cycles(G)
        self.assertFalse(has_cycle(G))



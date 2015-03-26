__author__ = 'dominick'

# Classes representing a directed (possibly cyclic) graph


class Node(object):
    def __init__(self, G):
        """
        Instantiates a node with parent graph G
        """
        # The parent graph of this node
        self._graph = G

        # Names of nodes pointing to this one
        self._inward = set()

        # Names of nodes to which this one points
        self._outward = set()

    def parent_graph(self):
        """
        :return: The graph associated with this node
        """
        return self._graph

    def inward_edges(self):
        """
        :return: An iterator over the set of names of nodes pointing to this node
        """
        return iter(self._inward)

    def outward_edges(self):
        """
        :return: An iterator over the set of names of nodes to which this node points
        """
        return iter(self._outward)

    def in_degree(self):
        """
        :return: The number of edges pointing into this node
        """
        return len(self._inward)

    def out_degree(self):
        """
        :return: The number of edges pointing out of this node
        """
        return len(self._outward)

    def has_edge_to(self, other):
        """
        :return: Whether there is an edge from this node to "other"
        """
        return other in self._outward

    def has_edge_from(self, other):
        """
        :return: Whether there is an edge to this node from "other"
        """
        return other in self._inward


class DiGraph(object):
    def __init__(self):
        """
        Instantiates a directed graph with no self-loops
        """

        # The set of nodes in the graph
        self.__nodes = {}

    def add_node(self, name):
        """
        Adds a node to the graph with the given name.
        Does nothing if there is already a node with this name.
        """
        self.__nodes[name] = Node(self)

    def add_edge(self, a, b):
        """
        Adds a directed edge from a to b.
        :raise: KeyError if a or b is not in the graph.
        :raise: AttributeError if a == b
        """
        if a not in self.__nodes:
            raise KeyError("Graph has no node named {}".format(a))
        if b not in self.__nodes:
            raise KeyError("Graph has no node named {}".format(b))
        if a == b:
            raise AttributeError("DiGraph does not support self-loops")
        node_a = self.__nodes[a]
        node_b = self.__nodes[b]
        node_a._outward.add(b)
        node_b._inward.add(a)

    def remove_edge(self, a, b):
        """
        Removes the directed edge from a to b
        :raise: KeyError if a or b is not in the graph.
        """
        if a not in self.__nodes:
            raise KeyError("Graph has no node named {}".format(a))
        if b not in self.__nodes:
            raise KeyError("Graph has no node named {}".format(b))

        if b in self.__nodes[a]._outward:
            self.__nodes[a]._outward.remove(b)
        if a in self.__nodes[b]._inward:
            self.__nodes[b]._inward.remove(a)

    def remove_node(self, name):
        """
        Removes the node with the given name from the graph
        :raise: KeyError if there is no node with the given name in the graph
        """
        if name not in self.__nodes:
            raise KeyError("Graph has no node named {}".format(name))

        node = self.__nodes[name]
        for i in list(node.inward_edges()):
            self.remove_edge(i, name)
        for i in list(node.outward_edges()):
            self.remove_edge(name, i)
        del self.__nodes[name]

    def __getitem__(self, name):
        """
        :return: The node with the given name
        :raise: KeyErros if there is no node with the given name in the graph
        """
        if name not in self.__nodes:
            raise KeyError("Graph has no node named {}".format(name))

        return self.__nodes[name]

    def __len__(self):
        """
        :return: The number of nodes in the graph
        """
        return len(self.__nodes)

    def contains_node(self, name):
        """
        :return: Whether the graph contains a node with the given name
        """
        return name in self.__nodes

    def contains_edge(self, a, b):
        """
        :return: Whether the graph contains a directed edge from a to b
        :raise: KeyError if a or b is not in the graph
        """
        if a not in self.__nodes:
            raise KeyError("Graph has no node named {}".format(a))
        if b not in self.__nodes:
            raise KeyError("Graph has no node named {}".format(b))

        return self.__nodes[a].has_edge_to(b)

    def __contains__(self, name):
        """
        :return: Whether the graph contains a node with the given name
        """
        return self.contains_node(name)

    def __iter__(self):
        """
        :return: An iterator over the nodes of the graph
        """
        return iter(self.__nodes)



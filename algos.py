__author__ = 'dominick'

from copy import deepcopy

from digraph import DiGraph


# Algorithms for finding an "optimal" topological sort on directed graphs


class CycleDetectedException(Exception):
    pass


def topological_sort(G: DiGraph):
    """
    Performs a topological sort on G.
    G is not modified.

    :return: A topological sort on G.
    :raise: CycleDetectedException if G contains a cycle.
    """
    G = deepcopy(G)
    n = len(G)
    L = []
    S = set(n for n in G if G[n].in_degree() == 0)

    while len(S) > 0:
        n = S.pop()
        L.append(n)

        for m in list(G[n].outward_edges()):
            G.remove_edge(n, m)
            if G[m].in_degree() == 0:
                S.add(m)

    if sum(G[n].in_degree() for n in G) > 0:
        raise CycleDetectedException()
    else:
        return L


def feedback_arc_set(G: DiGraph):
    """
    Calculates a feedback arc set S of G.
    That is, S is a set that contains an edge from all cycles in G.
    Implementation is based on
        http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.47.7745
    This set is not guaranteed to be minimum
    G is not modified.

    :return: A feedback arc set of G.
    """
    G = deepcopy(G)

    def find_source(G: DiGraph):
        for n in G:
            if G[n].in_degree() == 0:
                return True, n
        return False, None

    def find_sink(G: DiGraph):
        for n in G:
            if G[n].out_degree() == 0:
                return True, n
        return False, None

    s1 = []
    s2 = []

    while len(G) > 0:
        has_sink, sink = find_sink(G)
        while has_sink:
            s2.append(sink)
            G.remove_node(sink)
            has_sink, sink = find_sink(G)

        has_source, source = find_source(G)
        while has_source:
            s1.append(source)
            G.remove_node(source)
            has_source, source = find_source(G)

        if len(G) > 0:
            u = max(G, key=lambda n: G[n].out_degree() - G[n].in_degree())
            s1.append(u)
            G.remove_node(u)

    ret = []
    for j, n in enumerate(s1 + list(reversed(s2))):
        for i in range(j):
            ret.append((i, j))

    return ret

def remove_cycles(G: DiGraph):
    """
    Ensures that G is a DAG by removing the edges found in a feedback arc set
    Modifies G
    """
    to_remove = feedback_arc_set(G)
    print("removing edges:", to_remove)
    for (a, b) in to_remove:
        G.remove_edge(a, b)


def modified_topological_sort(G: DiGraph):
    """
    Attempts to perform a topological sort on G.
    If G contains a cycle, deletes edges until all cycles are removed,
    then re-runs topological sort.

    :returns: A topological sort on G, correct up to a cycle heuristic.
    """
    try:
        return topological_sort(G)
    except CycleDetectedException:
        remove_cycles(G)
        return topological_sort(G)

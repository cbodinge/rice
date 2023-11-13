class Node:
    def __init__(self, name, value=None):
        self.name = name
        self.value = value
        self.visited = False
        self.edges = {}
        self._ins = set()

    def out_to(self, node: 'Node', weight=None):
        edge = Edge(self, node, weight)
        self.edges[node] = edge
        node._ins.add(self)

    def in_frm(self, node: 'Node', weight=None):
        edge = Edge(node, self, weight)
        node.edges[self] = edge
        self._ins.add(edge)

    @property
    def in_deg(self):
        return len(self._ins)

    @property
    def out_deg(self):
        return len(self.edges)


class Edge:
    def __init__(self, a_node, z_node, weight=None):
        self.beg = a_node
        self.end = z_node
        self.weight = weight


class Graph:
    def __init__(self):
        self._nodes = {}
        self.fun = lambda x: x
        self._prefix = '   '

    def add_node(self, name, value=None):
        self._nodes[name] = Node(name, value)

    def directed(self, from_node, to_node, weight=None):
        node1 = self._nodes[from_node]
        node2 = self._nodes[to_node]
        node1.out_to(node2, weight)

    def undirected(self, node1, node2, weight=None):
        self.directed(node1, node2, weight)
        self.directed(node2, node1, weight)

    def _refresh(self):
        for node in self._nodes.values():
            node._visited = False

    def print(self):
        self._refresh()
        for node in self._nodes.values():
            if not node.visited:
                self._print(node)

    def _print(self, node, i=0):
        if node.visited:
            return

        node.visited = True
        print(i*self._prefix + node.name)

        for next_node in node.edges:
            self._print(next_node, i + 1)

        return

    @property
    def nodes(self):
        return self._nodes

from typing import Any, List, Tuple, Union

class Vertex:
    def __init__(self, value: Any):
        self.value = value

    def __repr__(self) -> str:
        return 'Vertex({})'.format(self.value)

class Edge:
    def __init__(self, source: Vertex, target: Vertex, weight: Union[int, None] = None):
        self.source = source
        self.target = target
        self.weight = weight

    def __repr__(self) -> str:
        return 'Edge({}->{})'.format(self.source, self.target)

    def reverse(self):
        """
        Returns a new `Edge` object with `source` and `target` swapped.
        """
        return Edge(self.target, self.source, self.weight)

class DirectedGraph:
    def __init__(self, vertices: List[Vertex], edges: List[Edge]) -> None:
        self.vertices = vertices
        self.edges = edges
        self.adjacency_list = self.create_adjacency_list(vertices, edges)

    @staticmethod
    def create_adjacency_list(vertices: List[Vertex], edges: List[Edge]) -> dict[Vertex, List[Vertex]]:
        adjlist: dict[Vertex, List[Vertex]] = {}
        for v in vertices:
            adjlist[v] = []
        for e in edges:
            adjlist.get(e.source, []).append(e.target)
        return adjlist


    def scc(self) -> List[set[Vertex]]:
        """
        Returns a list of strongly connected components (SCC) within the graph.
        Each SCC is returned as a set of `Vertex` objects.
        """

        # Reverse the graph so that sink SCCs become source SCCs.
        reverse_graph = self.reverse()

        # Use the postorder number to determine which nodes are source nodes
        # in the reverse graph. The greatest postorder number corresponds
        # to a source node.
        postorder = reverse_graph.postorder()

        # Run DFS on the original graph, exploring source nodes in order of 
        # descending postorder numbers. This guarantees that sink SCCs
        # are fully explored and marked as seen before exploring ancestor SCCs.
        visited: set[Vertex] = set()
        def explore(v: Vertex, connected_component: set):
            visited.add(v)
            connected_component.add(v)
            for target in self.adjacency_list.get(v, []):
                if target not in visited:
                    explore(target, connected_component)

        result = []
        for _, v in reversed(postorder):
            if v not in visited: 
                cc = set()
                explore(v, cc)
                result.append(cc)

        return result

    def postorder(self) -> List[Tuple[int, Vertex]]:
        """
        Returns a sorted list of tuples of `(postorder, Vertex)` for every 
        `Vertex` in the graph. Sorted by ascending postorder number.

        Note: the postorder number for each `Vertex` may change between
        different Graph instances that contain the same set of `Vertex` and
        `Edge`s. The only guarantee is that the greatest postorder 
        number will belong to a source node.
        """
        visited: set[Vertex] = set()
        result = []

        def explore(v: Vertex, postorder: int):
            visited.add(v)
            for target in self.adjacency_list.get(v, []):
                if target not in visited: 
                    postorder = explore(target, postorder)

            result.append((postorder, v))
            return postorder + 1

        postorder = 1
        for v in self.vertices:
            if v not in visited: 
                postorder = explore(v, postorder)

        return result

    def reverse(self) -> 'DirectedGraph':
        """
        Returns a Graph with all edges reversed.
        """
        return DirectedGraph(self.vertices, [e.reverse() for e in self.edges])

import unittest
from graphs.graph import Vertex, Edge, DirectedGraph

class TestDirectedGraph(unittest.TestCase):
    def create_test_graph(self):
        """
        Creates a test graph from CS6515 lectures.
        """
        a = Vertex("a")
        b = Vertex("b")
        c = Vertex("c")
        d = Vertex("d")
        e = Vertex("e")
        f = Vertex("f")
        g = Vertex("g")
        h = Vertex("h")
        i = Vertex("i")
        j = Vertex("j")
        k = Vertex("k")
        l = Vertex("l")
        vertices = [a, b, c, d, e, f, g, h, i, j, k, l]
        edges = [
                Edge(a, b),
                Edge(b, c),
                Edge(b, d),
                Edge(b, e),
                Edge(c, f),
                Edge(e, b),
                Edge(e, l),
                Edge(f, g),
                Edge(f, i),
                Edge(g, c),
                Edge(g, f),
                Edge(h, i),
                Edge(h, j),
                Edge(i, j),
                Edge(j, h),
                Edge(j, k),
                Edge(k, l),
                Edge(l, i),
                ]
        return DirectedGraph(vertices, edges)

    def test_postorder_simple(self):
        a = Vertex('a')
        aa = Vertex('aa')
        ab = Vertex('ab')
        ac = Vertex('ac')
        aaa = Vertex('aaa')
        aab = Vertex('aab')
        vertices = [a, aa, ab, ac, aaa, aab]
        edges = [
                Edge(a, aa),
                Edge(a, ab),
                Edge(a, ac),
                Edge(aa, aaa),
                Edge(aa, aab),
                ]
        graph = DirectedGraph(vertices, edges)
        postorder = graph.postorder()

        expected_order = [(1, aaa), (2, aab), (3, aa), (4, ab), (5, ac), (6, a)]
        self.assertListEqual(expected_order, postorder)

    def test_scc(self):
        graph = self.create_test_graph()
        print(graph.scc())


if __name__ == "__main__":
    unittest.main()

from manim import *

#GraphAlgorithms

class Show:
    def show(self, *vmobjs, scales=[0.7], delay=3, arrange=DOWN):
        group = Group()
        if len(scales) == 1 and len(vmobjs) > 1:
            scales = scales * len(vmobjs)
        for i in range(0, len(vmobjs)):
            group.add(vmobjs[i]).scale(scales[i]).arrange(arrange)
        print(scales)
        self.play(FadeIn(group))
        self.wait(delay)
        self.play(FadeOut(group))

class Elementary_Graph_Algorithms(Scene, Show):
    
    def construct(self):
        def representation_of_graph():
            self.show(Tex("lesson 6-1-1. Elementary Graph Algorithms"), Tex("This chapter presents methods for representing a graph and for searching a graph.Searching a graph means systematically following the edges of the graph so as to visit the vertices of the graph. A graph-searching algorithm can discover much about the structure of a graph. Many algorithms begin by searching their input graph to obtain this structural information. Several other graph algorithms elaborate  on basic graph searching. Techniques for searching a graph lie at the heart of the field of graph algorithms."))
            self.show(Graph([1, 2, 3, 4, 5], [(1, 2), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (4, 5)], layout="kamada_kawai", layout_scale=3, labels=True), Tex("This is an undirected graph G with 5 vertices and 7 edges"))
            self.show(ImageMobject("lesson6_1.png"), Tex("This is an adjacency-list representation of graph G"), scales=[6, 0.7])
            
            table = MathTable(
                [
                    ["/", 1, 2, 3, 4, 5],
                    [1, 0, 1, 0, 0, 1],
                    [2, 1, 0, 1, 1, 1],
                    [3, 0, 1, 0, 1, 0],
                    [4, 0, 1, 1, 0, 1],
                    [5, 1, 1, 0, 1, 0]
                ], include_outer_lines=False
            ).scale(0.7)
            table_text = Tex("This is the adjacency-matrix representation of G").next_to(table, DOWN)
            self.play(table.create(), FadeIn(table_text))
            self.wait(4)
            self.play(FadeOut(table, table_text))
            
            self.show(Tex("The adjacency-list representation of a graph G = (V, E) consists of an array Adj of |V| lists,\n one for each vertex in V. For each u in V , \n the adjacency list Adj[u] contains all the vertices such that there is an edge (u, v) in E. \n That is, Adj[u] consists of all the vertices adjacent to u in G."))
            self.show(Tex("If G is a directed graph, the sum of the lengths of all adjacency lists is |E|"),  Tex("If G is an undirected graph, the sum of the lengths of all the adjacency lists is 2 |E|"), Tex("For both directed and undirected graphs, the adjacency-list representation has the desirable property that the amount of memory it requires is O(V+E)."), scales=[1.1, 0.9, 0.8])
            self.show(Tex("We can readily adapt adjacency lists to represent weighted graphs, that is, graphs\nfor which each edge has an associated weight, typically given by a weight function w : E -> R"))
            self.show(Tex("A potential disadvantage of the adjacency-list representation is that it provides\nno quicker way to determine whether a given edge (u, v) is present in the graph\nthan to search for  in the adjacency list Adj[u]. An adjacency-matrix representation of the graph remedies this disadvantage, but at the cost of using asymptotically\nmore memory."))
            self.show(Tex("For the adjacency-matrix representation of a graph G = (V,E), we assume\nthat the vertices are numbered 1, 2, ..., |V| in some arbitrary manner. The nthe adjacency-matrix representation of a graph G consists of a |V| x |V| matrix").shift(UP), Tex(r"A = ($a_{ij}$) such that \\ $a_{ij} = \begin{cases} 1 & \text{if } (i,j) \in \text{E ,}\\  0 & \text{otherwise .}  \end{cases}$"))
            self.show(Tex("Like the adjacency-list representation of a graph, an adjacency matrix can represent a weighted graph. For example, if G = (V, E) is a weighted graph with edge-weight function w, we can simply store the weight w(u, v) of the edge (u, v) $\\in$ E as the entry in row u and column v of the adjacency matrix. If an edge does not exist, we can sotre a NIL value as its corresponding matrix entry, though for many problems it is convenient to use a value such as 0 or $\\infty$."))
            self.show(Tex("Although the adjacency-list representation is asymptotically at least as space-efficient as the adjavenvy-matrix representation, adjacency matrices are simpler, and so we may prefer them when graphs are reasonably small, Moreover, adjacency matrices carry a further advantage for unweighted graphs: they require only one bit per entry."))
        
        def bfs():
            self.show(Tex("lesson 6-1-2. Breadth-first search"), Tex("Breadth-first search is one of the simplest algorithms for searching a graph and the archetype for many important graph algorithms."))
            self.show(Tex("Graph a graph (V, E) and a distinguished source vertex s, breadth-first search systematically explores the edges of the edges of G To \"discover\" every vertex that is reachable from s. It computes the distance (smallest number of edges) from s to each reachable vertices. For any vertex v reachable from s, the simple path in the breath-first tree from s to v corresponds to a \"shortest path\" from s to v in G, that is, a path containing the smallest number of edges. The algorithm works on both directed and undirected graph."))
            self.show(Tex("Breadth-first search is so named because it expands the frontier between discovered and undiscovered vertices uniformly across the breadth of the frontier. Thta is, the algorithms discovers all vertices at distance k from s before discovering any vertices at distance k + l."))
            self.show(Tex("Breadth-first search constructs a breadth-first tree, initially containing only its root, which is the source vertex s. Whenever the search discovers a while vertex v in the course of scanning the adjacency list of an already discovered vertex u, the vertex v and the edge (u, v) are added to the tree. We say that u is the predecessor of parent of v in the breadth-first tree. Since a vertex is discovered at most one, it has at most one parent. Ancestor and descendant relationships in the breadth-first tree are definied relative to the root s as usual: if u is on the simple path in the tree from the root s to vertex v, then u is an ancestor of v and v is a descendant of u."))
            self.show(Tex("The breadth-first seach procedure BFS below assume that the input graph G = (V, E) is represented using adjacency lists. It attaches several additional attributes to each vertex in the graph. We store the color of each vertex u $\\in$ V in the attribute u.color and the prodecessor of u in the attribute u.$\\pi$. If u has no predecessor (for example, if u = s or u has not been discovered), then u.$\\pi$ = NIL. The attribute u.d holds the distance from the source s to vertex u computed by the algorithm. The algorithm also uses a first-in, first-out queue Q to manage the set of vertices."), ImageMobject("lesson6_2.png"), scales=[0.25, 2.25], arrange=RIGHT)
            self.show(ImageMobject("lesson6_3.png"), Tex("This is the operation of BFS on an undirected graph. Tree edges are shown shaded as they are produced by BFS. The value of u.d appears within each vertex u. The queue Q is shown at the beginning of each iteration of the while loop of lines 10–18. Vertex distances appear below vertices in the queue."), scales=[2.4, 0.7])
            self.show(Tex("The results of breadth-first search may depend upon the order in which the neighbors of a given vertex are visited in line 12: the breadth-first tree may vary, but the distances d computed by the algorithm will not. "))
            self.show(Tex("Before proving the various properties of breadth-first search, we take on the somewhat easier job of analyzing its running time on an input graph G = (V, E). We use aggregate analysis. After initialization, breadth-first search never whitens a vertex, and thus the test in line 13 ensures that each vertex is enqueued at most once, and hence dequeued at most once. The operations of nqueuing and dequeuing take O(1) time, and so the total time devoted to queue operations is O(V). Because the procedure scans the adjacency list of each vertex only when the vertex is dequeued, it scans each adjacency list at most once. Since the sum of the lengths of all the adjacency lists is E, the total time spent in scanning adjacency lists is O(E). The overhead for initialization is O(V), and thus the total running time of the BFS procedure is O(V + E). Thus, breadth-first search runs in time linear in the size of the adjacency-list representation of G."))
            self.show(Tex("At the beginning of this section, we claimed that breadth-first search finds the distance to each reachable vertex in a graph G = (V, E) from a given source vertex s $\\in$ V . Define the shortest-path distance 8(s, v) from s to v as the minimum number of edges in any path from vertex s to vertex ; if there is no path from s to v,then 8(s, v) = $\\infty$. We call a path of length 8(s, v) from s to v a shortest path from s to v. Before showing that breadth-first search correctly computes shortestpath distances, we investigate an important property of shortest-path distances."))
            self.show(Tex("The procedure BFS builds a breadth-first tree as it searches the graph. The tree corresponds to the $\\pi$ attributes."),
                      Tex("More formally, for a graph G = (V, E) with source s, we define the predecessor subgraph of G as "),
                      Tex(r"$G_{\pi } = \left ( V_{\pi }, E_{\pi } \right ), where$"), Tex(r"$V_{\pi } = \left \{ v \in V : v.\pi \neq NIL \right \}\ \cup \left \{ s \right \} and$"), Tex(r"$E_{\pi } = \left \{ \left ( v.\pi ,v \right ): v \in V_{\pi}-\left \{ s \right \} \right \}$"), scales=[1, 1, 0.8, 0.8, 0.8])
            
        representation_of_graph()
        bfs()    
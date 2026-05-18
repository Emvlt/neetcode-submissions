class DSU:
    # Disjoint-set data structures support three operations: 
    # Making a new set containing a new element
    # Finding the representative of the set containing a given element 
    # Merging two sets.
    def __init__(self):
        self.parent = defaultdict(tuple)
        self.vertices = set()
        self.rank = defaultdict(tuple)

    def add(self, vertex:tuple):
        self.vertices.add(vertex)
        self.parent[vertex] = vertex
        self.rank[vertex] = 0

    def find(self, vertex):
        if self.parent[vertex] == vertex:
            return vertex, self.rank[vertex]
        
        return self.find(self.parent[vertex])

    def union(self, v0, v1):
        p0, r0 = self.find(v0)
        p1, r1 = self.find(v1)

        if p0 == p1:
            return 

        if r0 < r1:
            p0, p1 = p1, p0

        self.parent[p1] = p0
        if r0 == r1:
            self.rank[p0] = r0 + 1
        

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        n = len(points)

        def distance(x, y):
            return abs(x[0]-y[0]) + abs(x[1]-y[1])

        nodes = {tuple(p) for p in points}

        edges = []

        for i in range(n-1):
            p0 = tuple(points[i])
            for j in range(i+1, n):
                p1 = tuple(points[j])
                edges.append((distance(p0, p1), p0, p1))

        edges.sort()
        
        total = 0
        dsu = DSU()

        for n in nodes:
            dsu.add(n)

        for cost, u, v in edges:
            (pu,_) , (pv, _) = dsu.find(u), dsu.find(v)
            if pu != pv:
                dsu.union(pu, pv)
                total += cost
                
        return total
import heapq 

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def norm(x, y):
            return x**2 + y**2

        heap = []

        for p in points:
            x = p[0]
            y = p[1]
            d = norm(x, y)

            if len(heap) < k:
                heapq.heappush_max(heap, (d, (x,y)))

            else:
                heapq.heappushpop_max(heap, (d, (x,y)))

        return [el[1] for el in heap]
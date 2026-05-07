class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # adjency list
        adj = [[] for i in range(numCourses)]
        for destination, source in prerequisites:
            adj[source].append(destination)

        visited = [0 for i in range(numCourses)]
        solutions = []

        def hasCycle(index):
            if visited[index] == 1:
                return True
            if visited[index] == 2:
                return False
            
            visited[index] = 1

            for n in adj[index]:
                if hasCycle(n):
                    return True            
            
            solutions.append(index)
            visited[index] = 2
            return False

        for index in range(numCourses):
            if visited[index] == 0:
                if hasCycle(index):
                    return []  

        return solutions[::-1]
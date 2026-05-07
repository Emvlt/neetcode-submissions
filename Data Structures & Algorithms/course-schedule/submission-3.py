class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Adjency list: adj[source] = [..., dest_i, ...]
        adj = [[] for _ in range(numCourses)]
        for dest, source in prerequisites:
            adj[source].append(dest)

        # Visitation
        # 0 = not visited
        # 1 = visiting
        # 2 = visited
        visited = [0 for _ in range(numCourses)]

        def hasCycle(index):
            if visited[index] == 1:
                return True
            if visited[index] == 2:
                return False

            visited[index] = 1
            for n in adj[index]:
                if hasCycle(n):
                    return True

            visited[index] = 2
            return False

        for i in range(numCourses):
            if visited[i] == 0:
                if hasCycle(i):
                    return False
        
        # We look for courses that cannot be taken. If we haven't found any, we can safely return True
        return True
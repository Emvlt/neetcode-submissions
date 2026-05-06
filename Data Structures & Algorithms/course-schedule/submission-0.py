class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Adjency list is a list of size numCourses
        # it takes the prequisites, and creates a mapping from source to destination
        # prerequisite[i] = [dest, src] 
        adjency = [[] for _ in range(numCourses)]
        for dest, src in prerequisites:
            adjency[src].append(dest)

        state = [0] * numCourses

        def has_cycle(v):
            if state[v] == 1: # Found a cycle!
                return True
            if state[v] == 2: # Already processed
                return False
            
            # Start visiting
            state[v] = 1
            for neighbor in adjency[v]:
                if has_cycle(neighbor):
                    return True

            ## Fully processed
            state[v] = 2
            return False
            

        for i in range(numCourses):
            if state[i] == 0:
                if has_cycle(i):
                    return False
        
        return True
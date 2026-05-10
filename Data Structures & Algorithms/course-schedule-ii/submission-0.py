class Solution:
    def getAdj(self, V: int, edges: List[List[int]]) -> dict:
        adj = {}
        for node in range(V):
            adj[node] = []
        for u, v in edges:
            adj[v].append(u)
        return adj

    def fillIndegree(self, adj: dict, indegree: List[int]) -> None:

        for neighbors in adj.values():
            for neighbor in neighbors:
                indegree[neighbor] += 1
    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = self.getAdj(numCourses, prerequisites)
        indegree = [0] * numCourses
        self.fillIndegree(adj, indegree)

        q = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        
        order = []
        while q:
            course = q.popleft()
            order.append(course)

            nextCourses = adj[course]

            for nextCourse in nextCourses:
                indegree[nextCourse] -= 1
                if indegree[nextCourse] == 0:
                    q.append(nextCourse)
        
        if len(order) != numCourses:
            return []
        return order





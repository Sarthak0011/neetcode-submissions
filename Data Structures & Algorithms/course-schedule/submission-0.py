class Solution:
    def getAdj(self, n: int, edges: List[List[int]]) -> dict:
        adj = {}
        for i in range(n):
            adj[i] = []

        for u, v in edges:
            adj[u].append(v)
        return adj
    
    def dfs(self, course: int, adj: dict, pathVisited: List[bool], visited: List[bool]) -> bool:
        if pathVisited[course]: return False
        if visited[course]: True

        visited[course] = True
        pathVisited[course] = True

        for prereq in adj[course]:
            if not self.dfs(prereq, adj, pathVisited, visited):
                return False

        pathVisited[course] = False

        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = self.getAdj(numCourses, prerequisites)
        visited = [False] * numCourses
        pathVisited = [False] * numCourses

        for i in range(numCourses):
            if not self.dfs(i, adj, pathVisited, visited):
                return False
        return True
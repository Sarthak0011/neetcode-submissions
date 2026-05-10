class Solution:
    def getAdj(self, V: int, edges: List[List[int]]) -> dict:
        adj = {}
        for node in range(V): adj[node] = []

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        return adj

    def dfs(self, node: int, adj: dict, visited: List[int]) -> None:
        visited[node] = True

        for neighbor in adj[node]:
            if not visited[neighbor]:
                self.dfs(neighbor, adj, visited)

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = self.getAdj(n, edges)
        visited = [False] * n

        components = 0 
        for i in range(n):
            if not visited[i]:
                self.dfs(i, adj, visited)
                components += 1
        return components
class Solution:
    def getAdj(self, V: int, edges: List[List[int]]) -> dict:
        adj = {}
        for node in range(V): adj[node] = []

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        return adj

    def dfs(self, node: int, prevNode: int, adj: dict, visited: List[bool]) -> bool:
        if visited[node]:
            return False
        
        visited[node] = True

        neighbors = adj[node]

        for neighbor in neighbors:
            if neighbor != prevNode:
                flag = self.dfs(neighbor, node, adj, visited)
                if not flag: return False
        
        return True

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = self.getAdj(n, edges)
        visited = [False] * n
        flag = self.dfs(0, -1, adj, visited)
        if not flag: return False

        for val in visited:
            if not val: return False
        return True




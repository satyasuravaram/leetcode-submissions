class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:   
        
        if not edges:
            return [0]
        
        # Set up adjacency list
        adj = [set() for _ in range(n)]
        for i, j in edges:
            adj[i].add(j)
            adj[j].add(i)
        
        # Get initial leaf nodes
        leaves = []
        for i in range(n):
            if len(adj[i]) == 1:
                leaves.append(i)
        
        # Keep removing outer leaves
        while n > 2:
            n -= len(leaves)
            newLeaves = []
            for c in leaves:
                p = adj[c].pop()
                adj[p].remove(c)
                if len(adj[p]) == 1:
                    newLeaves.append(p)
            leaves = newLeaves
            
        return leaves
        
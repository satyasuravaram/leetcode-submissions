class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        visited = set()
        ans = 0
        
        def dfs(n):
            if n in visited:
                return
            visited.add(n)
            for i in range(len(isConnected[n-1])):
                if isConnected[n-1][i] == 1:
                    dfs(i+1)
        
        for n in range(1, len(isConnected) + 1):
            if n not in visited:
                dfs(n)
                ans += 1
        
        return ans
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        longest = [[1 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        visited = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        
        def findLongest(i, j):
            if visited[i][j]: 
                return
            visited[i][j] = True 
            cur = 1
            for x, y in [(0,1), (1, 0), (0, -1), (-1, 0)]:
                if i + x >= len(matrix) or i+x < 0 or j + y >= len(matrix[i]) or j+y < 0 or matrix[i+x][j+y] <= matrix[i][j]: 
                    continue
                findLongest(i+x, j+y)
                cur = max(cur, 1 + longest[i+x][j+y])
            longest[i][j] = cur
           
        longestPath = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if not visited[i][j]:
                    findLongest(i, j)
                longestPath = max(longestPath, longest[i][j])
        return longestPath
        
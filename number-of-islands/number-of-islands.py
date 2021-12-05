class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        def markIsland(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == "0" or (i, j) in visited:
                return
            visited.add((i, j))
            markIsland(i+1, j)
            markIsland(i-1, j)
            markIsland(i, j+1)
            markIsland(i, j-1)
        
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i, j) not in visited and grid[i][j] == "1":
                    markIsland(i, j)
                    islands += 1
        return islands
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_count = 0
        def _dfs(y,x):
            if y < 0 or x < 0:
                return
            if y >= len(grid) or x >= len(grid[0]):
                return
            if grid[y][x] == "0":
                return
            if grid[y][x] == "1":
                grid[y][x] = 2
                _dfs(y,x+1)
                _dfs(y+1,x)
                _dfs(y-1,x)
                _dfs(y,x-1)      
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == "1":
                    num_count +=1
                    _dfs(y,x)
        return num_count
       # Easy DFS with optimization 
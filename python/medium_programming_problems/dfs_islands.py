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
       # 
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # We are going to solve with BFS
        num_islands = 0
        # Iterate through each element, if we find a '1' we BFS and increment
        # During our BFS, we increment each land_mass to be a 2 - stating we have been here before
        # if we encounter a 2 in our iteration, we skip over it
        MAX_Y = len(grid)
        MAX_X = len(grid[0])
        for y in range(MAX_Y):
            for x in range(MAX_X):
                if grid[y][x] == "1":
                    # Cool! We are in BFS territory
                    num_islands +=1
                    queue = deque()
                    queue.append((y,x))
                    directions = [(0,1),(1,0),(0,-1),(-1,0)]
                    while queue:
                        cur_y, cur_x = queue.popleft()
                        for d in directions:
                            n_y, n_x = cur_y + d[0], cur_x + d[1]
                            if MAX_Y > n_y >= 0 and MAX_X > n_x >= 0:
                                # Valid point in grid
                                if grid[n_y][n_x] == "1":
                                    #Mark and add to BFS
                                    grid[n_y][n_x] = "2"
                                    queue.append((n_y, n_x))
        return num_islands
        # Fucking BFS Version for those who love indentation                                    
                                
                
         
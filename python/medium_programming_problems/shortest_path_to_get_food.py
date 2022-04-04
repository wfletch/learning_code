class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        # This is a simple BFS
        # I am going to use the double_queue technique
        queue = []
        step_count = 0
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        MAX_Y,MAX_X = len(grid), len(grid[0])
        #Initial Condition
        for y in range(MAX_Y):
            for x in range(MAX_X):
                if grid[y][x] == '*':
                    queue.append((y,x))
        
        while queue:
            step_count +=1
            next_queue = []
            for y,x in queue:
                for d in directions:
                    new_y,new_x = y + d[0], x + d[1]
                    if 0 <= new_y < MAX_Y and 0 <= new_x < MAX_X:
                        if grid[new_y][new_x] == '#':
                            return step_count
                        if grid[new_y][new_x] == 'O':
                            grid[new_y][new_x] = 'X'
                            next_queue.append((new_y,new_x))
            queue=next_queue
        return -1

       # LC # 1730
       # Time : O(mn)
       # Space: O(mn)
       # # Looking good 
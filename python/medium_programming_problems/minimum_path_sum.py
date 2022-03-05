class Solution:
    memo = None
    enabled = True
    def findMinSum(self, grid, loc=[0,0]):
        # Useful shorthands
        x , y = loc
        cost = grid[y][x]
        # Terminal Condition
        if y == len(grid) -1 and x == len(grid[0]) -1:
            return cost
        # Otherwise, calculate cost
        # Check if we have already got cost
        # Can we move down
        if y + 1 == len(grid):
            d_cost = float('inf')
        else:
            # We can travel down, let's do it:
            # Firs check for mem
            if self.memo[y + 1][x] != -1 and self.enabled:
                d_cost = self.memo[y + 1][x]
            else:
                d_cost = self.findMinSum(grid, [x, y+1])
         # Can we Move Right
        if x + 1 == len(grid[0]):
            r_cost = float('inf')
        else:
            # First check for mem
            if self.memo[y][x + 1] != -1 and self.enabled:
                r_cost = self.memo[y][x + 1]
            else:
                # We can travel down, let's do it:
                r_cost = self.findMinSum(grid, [x+1, y])
                
        # we have returned from looking ahead
        min_val = cost + min(r_cost, d_cost)
        if self.memo[y][x] == -1 or min_val < self.memo[y][x]:
            self.memo[y][x] = min_val
        return min_val
    
    def minPathSum(self, grid: List[List[int]]) -> int:
        self.memo = [[-1 for _ in range(len(grid[0]))] for i in range(len(grid))]
        min_v = self.findMinSum(grid)
        return(min_v)
        # WIP

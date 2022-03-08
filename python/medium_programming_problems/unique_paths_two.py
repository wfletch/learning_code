class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # DFS, but if we find an obstacle, End Early
        # Follow Up: memoize
        # Follow Up: We could Memoize on the current obstacleGrid!
        memo = [[-1 for x in obstacleGrid[0]] for y in obstacleGrid]
        memo[-1][-1] = 1
        def dfs(y = 0, x = 0):
            cur_loc = obstacleGrid[y][x]
            if cur_loc == 1:
                # We are at an obstacle
                return 0
            elif y == len(obstacleGrid)-1 and x == len(obstacleGrid[0])-1:
                # We are at our target destination
                return 1
            else:
                d_path = 0
                r_path = 0
                if memo[y][x] > -1:
                    return memo[y][x]
                if y + 1 < len(obstacleGrid):
                    # We can still go down
                    d_path = dfs(y+1,x)
                if x + 1 < len(obstacleGrid[0]):
                    # We can still go down
                    r_path = dfs(y,x+1)
                memo[y][x] = d_path + r_path
                return d_path + r_path
        return dfs()
        # LC # 63
        # Time Complexity : O(mn) # need to iterate through the list
        # Space Complexity: O(mn). But it can be reduced to O(1) if I use the
        # Supplied Grid as the memoization matrix
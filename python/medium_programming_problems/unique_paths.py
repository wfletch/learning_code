class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # DFS with Memoization to remember available options from that point onwards
        # Bottom Up DFS
        m = m-1
        n = n-1
        memo = [[-1 for x in range(n+1)] for y in range(m+1)]
        memo[-1][-1] = 1
        def dfs(y = 0,x = 0):
            if y == m and x == n: # We are at the end Goal
                return 1
            else:
                y_count = 0
                x_count = 0
                if memo[y][x] != -1:
                    return memo[y][x]
                if y != m: # We can still go down
                    y_count = dfs(y+1, x)
                if x != n: # We can still go right
                    x_count = dfs(y, x+1)
                memo[y][x] = y_count + x_count
                return y_count + x_count
        dfs()
        print(memo)
        return memo[0][0]
        
# LC # 62
# Time Complexity: O(mn)
# Space Complexity: O(mn)
# Notes: This was rather straightforward DFS + DP optimization
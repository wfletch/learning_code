class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        directions = [(-1,1), (-1,0) ,(-1,-1), (0,1),(0,-1), (1,1), (1,0), (1,-1)]
        grid = [["." for i in range(n)] for k in range(n)]
        def _check_queen(grid, y,x): # This is expensive, but there is a constant time optimization
            # Check if we can place a queen here
            # Check left
            for d in directions:
                y_2, x_2 = y,x
                while n > x_2 >= 0 and n > y_2 >= 0:
                    if grid[y_2][x_2] == 'Q':
                        return False
                    y_2+= d[0]
                    x_2+= d[1]
            return True
        solutions = []
        def _backtrack(grid = grid,y=0,x=0,num=0):
            # Try place at evey given point
            if num == n:
                # The current grid is a candidate
                solutions.append(["".join(i) for i in grid])
                return
            for a in range(0,n):
                for b in range(0,n):
                    if a <= y and b <= x: # Catch up to where we are.
                        continue
                    if _check_queen(grid,a,b):
                        # We can place here
                        # Place
                        grid[a][b] = 'Q'
                        _backtrack(grid=grid,y=a,x=b,num=num+1)
                        # Unplace
                        grid[a][b] = '.'
        _backtrack()
        return solutions
       # This is simple n-queens
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Two set method
        # have an active and a passive set
        # If, after we switch sets we have nothing in our active set, we are done.
        active, passive = set(),set()
        fresh_orange_count = 0
        minutes = -1
        # initial conditions
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 2:
                    # Initial rotten orange
                    active.add((y,x))
                if grid[y][x] == 1:
                    fresh_orange_count +=1
        if fresh_orange_count == 0:
            return 0
        while len(active) != 0:
            for y,x in active:
                # Is this fresh, minus one from our fresh_count
                if grid[y][x] == 1:
                    fresh_orange_count -=1
                grid[y][x] = 2 # Poison
                # Make sure the point is in the grid and we are not double processing
                if x-1 >= 0 and grid[y][x-1] == 1 and (y,x-1) not in active:
                    passive.add((y,x-1))
                if y-1 >= 0 and grid[y-1][x] == 1 and (y-1,x) not in active:
                    passive.add((y-1,x))
                if x + 1 < len(grid[0]) and grid[y][x+1] == 1 and (y,x+1) not in active:
                    passive.add((y,x+1))
                if y + 1 < len(grid) and grid[y+1][x] == 1 and (y+1,x) not in active:
                    passive.add((y+1,x))
            active = set()
            minutes +=1
            active,passive = passive,active
        return -1 if fresh_orange_count else minutes
                
                    
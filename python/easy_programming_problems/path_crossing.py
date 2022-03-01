class Solution:
    def isPathCrossing(self, path: str) -> bool:
        #Hash every x,y location
        location = {(0,0) : 1}
        x = 0
        y = 0
        for i in path:
            if i == 'N':
                y += 1
            if i == 'S':
                y -= 1
            if i == 'E':
                x += 1
            if i == 'W':
                x -= 1
            if (x,y) in location:
                return True
            location[(x,y)] = 1
        return False
        
# Leet Code 1496
# Time Complexity: O(n)
# Space Complexity: O(n)
# Could I Do better?
#   I can reduce space by increasing time to n^2 by recalculating where I am (from Origin) after each new addition
#   And comparing if that location ever hits my current location
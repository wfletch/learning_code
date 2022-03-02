class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # Check if gradient is the same? Or identical Differential?
        # Calculate Adjacent Gradients
        if coordinates[1][1] - coordinates[0][1] == 0:
            base_grad = -1
        else:
            base_grad = (coordinates[1][0] - coordinates[0][0]) / (coordinates[1][1] - coordinates[0][1])
        for i in range(1 ,len(coordinates)-1, 1):
            # We need to see if we are doing 90 angle lines!
            if coordinates[i+1][1] - coordinates[i][1] == 0:
                # Div By 0!
                grad = -1
            else:
                grad = (coordinates[i+1][0] - coordinates[i][0]) / (coordinates[i+1][1] - coordinates[i][1])
            if grad != base_grad:
                return False
        return True
# LeetCode: 1232
# Time Complexity: O(n)
# Space Complexity: O(1) to store previous gradient
# I don't think it can be optimized anymore, without using some language specific trickery
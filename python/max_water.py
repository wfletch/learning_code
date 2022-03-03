class Solution:
    def maxArea(self, height: List[int]) -> int:
        l_pointer = 0
        r_pointer = len(height)-1
        total = 0
        while l_pointer < r_pointer:
            l = height[l_pointer]
            r = height[r_pointer]
            h = min(l,r)
            cur = h * (r_pointer-l_pointer)
            if cur > total:
                total = cur
            if l > r:
                r_pointer -=1
            else:
                l_pointer +=1
        return total

# Leet Code # 11
# Time Complexity: O(N)
# Space Complexity: O(1)
# Some lessons Learned: Simplify your thinking and implement easy solutions first
# Then I can waste 2 hours overthinking the problem
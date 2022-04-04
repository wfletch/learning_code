class Solution:
    def arraySign(self, nums: List[int]) -> int:
        val = 1
        for i in nums:
            if i < 0:
                val *= -1
            if i == 0:
                return 0
        if val > 0:
            return 1
        else:
            return -1
       # Eh. 
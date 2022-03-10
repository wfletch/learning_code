class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #Brute Force (Ish)
        # Would be to try all combinations in a tree like manner
        values = []
        def ftsw(nums = nums, target = target):
            if len(nums) == 0:
                if target == 0:
                    values.append(1)
            else:
                # Two options. Subtract and Plus
                s_option = ftsw(nums[1:], target+nums[0])
                a_option = ftsw(nums[1:], target-nums[0])
        ftsw()
        return len(values)
        # It works But it is slow
        # Time O(2^n)
        # Space O(n)

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #Brute Force (Ish)
        # Would be to try all combinations in a tree like manner
        values = []
        total = sum(nums)
        memo = collections.defaultdict(lambda: collections.defaultdict(lambda:-1))
        def ftsw(nums = nums, target = target, index = 0):
            if len(nums) == 0:
                if target == 0:
                    return 1
                else:
                    return 0
            else:
                if memo[index][target + total] > -1:
                    return memo[index][target + total]
                # Two options. Subtract and Plus
                
                s_option = ftsw(nums[1:], target+nums[0], index +1)
                a_option = ftsw(nums[1:], target-nums[0], index +1)
                memo[index][target + total] = s_option + a_option
                return  memo[index][target + total]
        values = ftsw()
        return values
        # It works But it is slow
        # Time O(memo)
        # Space O(memo)
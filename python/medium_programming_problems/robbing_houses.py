class Solution:
    memo = []
    def _rob(self, nums):
        house_num = len(nums)-1
        if self.memo[house_num] != -1:
            return self.memo[house_num]
        # Now, How can we memoize!
        if nums == []:
            return 0
        else:
            robbed = nums[-1] + self._rob(nums[:-2])
        # Rob (Move 2)
            not_robbed = self._rob(nums[:-1])
        # Don't Rob (Move 1)
        self.memo[house_num] = max(robbed, not_robbed, self.memo[house_num])
        return max(robbed, not_robbed)
    def rob(self, nums: List[int]) -> int:
        self.memo = [-1 for k in nums]
        k = self._rob(nums)
        return k
        
# Space: O(NM) Space of Memo * Space of Recursion
# Time: O(N) To Move Through the list!
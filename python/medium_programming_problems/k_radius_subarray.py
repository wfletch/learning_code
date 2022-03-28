class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        # Pre populate
        if k == 0:
            return nums
        avgs = [-1] * len(nums)
        if (2*k + 1) > len(nums):
            return avgs
        loc = k
        # We can only populate from 0 + k to len(nums) - k
        width = (2 * k) + 1
        cur_sum = sum(nums[0:width])
        avgs[loc] = cur_sum//width
        loc+=1
        left = 0
        right = width-1
        while loc < len(nums) - k:
            cur_sum -= nums[left]
            left+=1
            right+=1
            cur_sum += nums[right]
            avgs[loc] = cur_sum//width
            loc+=1
        return avgs
        # Works
        # Be careful on the numbers! 
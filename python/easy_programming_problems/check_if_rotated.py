class Solution:
    def check(self, nums: List[int]) -> bool:
        # Find the 1 location (Or Minimum)
        # Iterate over the length of the array starting at 1 location and check if is sorted
        min_val = min(nums)
        start_loc = nums.index(min_val)
        print(start_loc)
        indices = [i for i, x in enumerate(nums) if x == min_val]
        found = True
        for k in indices: # We can Have Duplicate Starting Points!!!!
            found = True
            for i in range(len(nums)-1):
                if nums[(i + k +1) % len(nums)] >= nums[(i + k) % len(nums)]:
                    continue
                else:
                    found =  False
                    break
            if found:
                return True
        return False
# LeetCode: 1752
# Time: O(N * Number of duplicated) + O(N) to find min locations
# Space: O(1)
# Can I optimize: If I knew the lowest value in the beginning I could just iterate through until I find one of those
# I do not think I can make this more optimal
            
        
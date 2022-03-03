class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        if len(nums) == 2:
            a = nums[0]
            b = nums[1]
            return [[a,b],[b,a]]
        else:
            permutations = []
            for i,v in enumerate(nums):
                pick = nums[i]
                left_over = nums[0:i]
                if i != len(nums)-1:
                    for k in nums[i+1:]: # Better way to slice this?
                        left_over.append(k)
                options = self.permute(left_over)
                for entry in options:
                    new_value = [pick]
                    for k in entry:
                        new_value.append(k)
                    permutations.append(new_value)
            return permutations
# Leet Code # 46
# This Is, by far, the most trivial way to compute permutations (Although, I don't know of any others off hand)
# While it has great memory footprint. It is rather slow
# A Better way to do this would be on the segmentation of follow-up permutations.
# We could use a swap instead of this new compound array appending!
# Time Complexity: O(K Pick N Permutations)
# Space Complexity: O(N x N!) N space (kind of....) for each option and N! Many options:34

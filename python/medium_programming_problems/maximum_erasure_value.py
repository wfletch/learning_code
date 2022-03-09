class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l_pointer = 0
        r_pointer = 1
        cur_max = 0
        def get_max_value(l_pointer, r_pointer):
            return sum(nums[l_pointer: r_pointer+1])
        cur_hash = {nums[l_pointer]:1}
        while r_pointer != len(nums):
            if nums[r_pointer] in cur_hash:
                # We have a collision!
                # Get Current Sum
                # Set l_pointer +=1
                # Set r_pointer = l_pointer
                cur_sum = get_max_value(l_pointer, r_pointer-1)
                cur_max = max(cur_max, cur_sum)
                cur_hash = {}
                l_pointer +=1
                r_pointer = l_pointer
            else:
                cur_hash[nums[r_pointer]] = 1
                r_pointer+=1
        # At the end, we have one more round
        cur_sum = get_max_value(l_pointer, r_pointer-1)
        cur_max = max(cur_max, cur_sum)
        return cur_max
        # This is the Naive Solution. It is slow at larget numbers of nums. It runs in user submission, but not when submitted to the auditor
        # Took about 15 minutes to implement. So I'm not worried about that.
        # Space Complexity is Linear
        # Time Complexity is O(n^2)
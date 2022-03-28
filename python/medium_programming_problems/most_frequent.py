class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # For each initial candidate, we try and count how many others can do it
        # N^2 solution. Go through each iteration and check if we can make matches
        # Something tells me, I want to sort this.
        nums.sort()
        nums.reverse()
        max_count = 0
        # We can only increment.
        # We can only move forward
        # This should time out.
        for i in range(len(nums)):
            target = nums[i]
            incs = k
            count = 1
            for j in range(len(nums)):
                if j <=i : continue
                incs -= (target - nums[j])
                if incs > -1:
                    count+=1
                else:
                    break
            max_count = max(count, max_count)
        return max_count
    # While this works, it is too slow for our use cases 

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # Sort
        nums.sort(reverse=True)
        # Great, now let's do something cool
        left = 0
        right = 1
        target = nums[left]
        maximum_count = 1
        cur_count = 1
        while right < len(nums):
            if k - (target - nums[right]) >= 0:
                # We can add this number to our count
                k -= (target - nums[right])
                cur_count +=1 
            else:
                # We can't we need to shift our target
                maximum_count = max(cur_count, maximum_count)
                old_target = target
                target = nums[left + 1]
                left +=1
                cur_count -=1
                # Regain k
                k += (old_target - target) * (right - left)
                continue
            right +=1
        maximum_count = max(cur_count, maximum_count)
        return maximum_count
        # Actually, flipping this around is WAAAAAY better!    
        
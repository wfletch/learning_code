class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        num_removals = 1
        for i in range(1,len(nums),1):
            cur_val = nums[i]
            prev_val = nums[i-1]
            # print(cur_val, prev_val)
            if cur_val > prev_val:
                continue
            else:
                if num_removals > 0:
                    if i +1 == len(nums):
                        return True
                    if i -2 < 0:
                        num_removals -=1
                        continue
                    if nums[i+1] > prev_val:
                        num_removals -=1
                        continue
                    else:
                        second_prev_value = nums[i-2]
                        if cur_val > second_prev_value:
                            num_removals -=1
                            continue
                        else:
                            return False
                else:
                    return False
        return True
# Leet Code # 1909
# Time Complexity: O(n). Need to iterate through the array
# Space Complexity: O(1). Constant number of values to compare
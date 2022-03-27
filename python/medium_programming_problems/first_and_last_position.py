class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Routine Iterative Binary Search
        def b_search(nums, target):
            left, right = 0, len(nums)-1
            while left <= right:
                pivot = left + (right - left) // 2
                if nums[pivot] == target:
                    return pivot
                elif nums[pivot] > target:
                    right = pivot -1
                else:
                    left = pivot +1
            return -1
        # Mid is a misnomer. It's more... mid..ish
        mid_point = b_search(nums,target)
        if mid_point == -1:
            return [-1,-1]
        results = []
        # We have the mid point!
        # Let's see if we can find a low_point
        max_low_point = mid_point
        true_low_point = -1
        while True:
            low_nums = nums[0:max_low_point]
            if low_nums == []:
                break
            true_low_point = b_search(low_nums, target)
            if true_low_point == -1:
                break
            max_low_point = true_low_point
        results.append(max_low_point)
        # Let's see if we can find a high_point
        min_high_point = mid_point
        true_high_point = -1
        while True:
            high_nums = nums[min_high_point+1:]
            if high_nums == []:
                break
            true_high_point = b_search(high_nums, target)
            if true_high_point == -1:
                break
            min_high_point+=(true_high_point +1)
        if min_high_point > mid_point:
            results.append(min_high_point)
        else:
            results.append(mid_point)
        return results
        
       # LC # 37
       # Time: O(lg(n))
       # Space: O(n) But I can reuse the existing array to optimize 
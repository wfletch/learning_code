class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if nums[pivot] == target:
                return pivot
            elif nums[pivot] > target:
                # We need to adjust our right
                right = pivot - 1
            else:
                left = pivot + 1
        return -1

    # Ye typical Iterative b_search 
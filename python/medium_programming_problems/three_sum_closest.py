class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closeset_diff = 10000
        closeset_candidate = -1000
        for i in range(len(nums)):
            cur_val = nums[i]
            # Iterate through the 'rest' of the array and two-pointer search for possible values
            l_pointer = i+1
            r_pointer = len(nums)-1
            while l_pointer < r_pointer:
                candidate = cur_val + nums[l_pointer] + nums[r_pointer]
                diff = abs(target-candidate)
                if diff < closeset_diff:
                    closeset_diff = diff
                    closeset_candidate = candidate
                # If we are below the target sum. move l_pointer up
                # If we are aboce the target sum. move r_pointer down
                if candidate > target:
                    r_pointer -=1
                elif candidate < target:
                    l_pointer +=1
                else:
                    return candidate
        return closeset_candidate
       # LC #16
       # Time Complexity (N^2) Using two pointer technique and some sorting
       # Space Complexity O(1)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Obvious Quadratic Solution would just be to find all unique sums
        # Modification of 3 sum would make it N^3 which is better.
        nums.sort()
        options = set()
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j <= i:
                    continue
                l_pointer = j+1
                r_pointer = len(nums)-1
                val_1 = nums[i]
                val_2 = nums[j]
                while l_pointer < r_pointer:
                    val_3 = nums[l_pointer]
                    val_4 = nums[r_pointer]
                    candidate = sum([val_1,val_2,val_3,val_4])
                    if candidate == target:
                        options.add((val_1,val_2,val_3,val_4))
                        # Cannot just break.
                        l_pointer +=1
                    elif candidate > target:
                        r_pointer -=1
                    else:
                        l_pointer +=1
        return options # I think we can optmize here.
       # LC # 18
       # Time Complexity: O(n^3)
       # Space Complexity: O(n)
        
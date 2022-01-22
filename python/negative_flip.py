class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        # First things first. Sort this boy
        nums.sort()
        cur_loc = 0
        last_flip_loc = 0
        while k > 0:
            if cur_loc >= len(nums):
                cur_loc = 0
            if nums[cur_loc] == 0:
                k = 0
            elif nums[cur_loc] < 0:
                # We are 100% going to flip
                k-=1
                nums[cur_loc]*=-1
                last_flip_loc = cur_loc
                cur_loc+=1
            elif nums[cur_loc] > 0:
                # We need to check if this value is currently smaller than our prev
                # flipped value
                # If it is. Continue flipping this one, if Not. Flip the previous one
                if nums[cur_loc] >= nums[last_flip_loc]:
                    # We need to flip the last flipped one
                    nums[last_flip_loc] *=-1
                    k-=1
                    while k > 0:
                        k-=1
                        nums[last_flip_loc]*=-1
                else:
                    nums[cur_loc]*=-1
                    k-=1
                    # At this point, we have found the lowest number!
                    # We can caontinue flipping until we reach 0
                    while k > 0:
                        k-=1
                        nums[cur_loc]*=-1
        print(nums)
        return sum(nums)
            
                
            
        

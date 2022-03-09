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
        # LC: 1695
        # This is the Naive Solution. It is slow at larget numbers of nums. It runs in user submission, but not when submitted to the auditor
        # Took about 15 minutes to implement. So I'm not worried about that.
        # Space Complexity is Linear
        # Time Complexity is O(n^2)

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l_pointer = 0
        r_pointer = 1
        level = 1
        cur_max = 0
        def get_max_value(l_pointer, r_pointer):
            return sum(nums[l_pointer: r_pointer+1])
        cur_hash = {nums[l_pointer]:level}
        cur_sum = nums[l_pointer]
        while r_pointer != len(nums):
            if cur_hash.get(nums[r_pointer], 0) == level:
                # We have a collision!
                # Get Current Sum
                # Set l_pointer +=1
                # Set r_pointer = l_pointer
                #cur_sum = get_max_value(l_pointer, r_pointer-1)
                cur_max = max(cur_max, cur_sum)
                level+=1
                if nums[r_pointer] == nums[l_pointer]:
                    l_pointer+=1
                else:
                    for i in range(l_pointer+1, r_pointer+1,1):
                        if nums[i] == nums[r_pointer]:
                            l_pointer = i
                            break
                #l_pointer = nums[l_pointer:r_pointer+1].index(nums[r_pointer])
                r_pointer = l_pointer
                cur_sum = 0
            else:
                cur_sum += nums[r_pointer]
                cur_hash[nums[r_pointer]] = level
                r_pointer+=1 
                
        # At the end, we have one more round
        #cur_sum = get_max_value(l_pointer, r_pointer-1)
        cur_max = max(cur_max, cur_sum)
        return cur_max
        # Slightly More Optimal Solution, But still not good enough

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l_pointer = 0
        r_pointer = 1
        cur_max = 0
        cur_hash = set()
        cur_hash.add(nums[l_pointer])
        cur_sum = nums[l_pointer]
        
        while r_pointer != len(nums):
            if nums[r_pointer] in cur_hash:
                cur_max = max(cur_max, cur_sum)
                if nums[r_pointer] == nums[l_pointer]:
                    cur_sum-= nums[l_pointer]
                    cur_hash.discard(nums[l_pointer])
                    l_pointer+=1
                else:
                    for i in range(l_pointer, r_pointer+1,1):
                        cur_sum-= nums[i]
                        cur_hash.discard(nums[i])
                        if nums[i] == nums[r_pointer]:
                            l_pointer = i+1
                            break
                #l_pointer = nums[l_pointer:r_pointer+1].index(nums[r_pointer])
                #r_pointer = l_pointer
                #cur_sum = 0
            else:
                cur_sum += nums[r_pointer]
                cur_hash.add(nums[r_pointer])
                r_pointer+=1 
                
        # At the end, we have one more round
        #cur_sum = get_max_value(l_pointer, r_pointer-1)
        cur_max = max(cur_max, cur_sum)
        return cur_max
        # Boom. USed a Set and counted up and down. Optimal.
        # O(N) Time. Technically O(2n)
class Solution:

    def __init__(self, nums: List[int]):
        self.array = nums
        self.orig = list(nums) #Duplicate the lst

    def reset(self) -> List[int]:
        self.array = self.orig
        self.orig = list(self.orig)
        return self.array

    def shuffle(self) -> List[int]:
        #Fischer-Yates Shuffle
        for i in range(len(self.array)):
            # Create a random number between i and length of array
            swap_idx = random.randrange(i,len(self.array))
            # Swap the values
            self.array[i], self.array[swap_idx] = self.array[swap_idx], self.array[i]
        return self.array

# Leet Code: 384
# Time Complexity: O(N)
# Space Complexity: O(N)
# This is just a garden variety implementation of Fischer-Yates
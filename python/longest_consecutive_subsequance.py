class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Counting sort?
        # Build a Min Heap?
        # Hash each value
        # Get Min from our single pass
        # Check hash for adjacent values
        # Stop once we dont have anythin
        if nums == []:
            return 0
        n = {}
        for i in nums:
            n[i] = 1
        # Before we return count, we might not have the longest sequance!
        # We need to iterate over all the keys and check if we have a longer
        # Valid answer
        # We will do this by checking for adjacent values being in the hash, if they are. we will mark them as being part of our sequance and skip
        count = 0
        for k in n.keys():
            if n[k] == -1:
                continue
            else:
                n[k] = -1
                temp_count = 1
                while n.get(k + temp_count, None) != None:
                    # Search 'up' for more continuity
                    n[k + temp_count] = -1
                    temp_count +=1
                up_count = temp_count
                temp_count = 0
                while n.get(k - temp_count, None) != None:
                    # Search 'down' for more continuity
                    n[k - temp_count] = -1
                    temp_count +=1
                up_count += temp_count
                if up_count > count:
                    count = up_count
        return count-1 #<-!!!!!!!???? WHY? Oh wait, we double count.
    
# Leet Code: 128
# Time Complexity O(2n) Iterate through List to build hash. iterate through hash
# Space Complexity O(n) Additional Hash of values required.
# Lessons Learned: Dont forget about hash maps! Memory is cheap!
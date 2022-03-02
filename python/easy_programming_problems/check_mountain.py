class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        rising = True
        one_rise = False
        for v in range(1,len(arr),1):
            if arr[v] == arr[v-1]:
                return False
            if arr[v] > arr[v-1]:
                one_rise = True
                if rising:
                    continue  
                else:
                    return False
            else:
                rising = False
                continue
        if rising or not one_rise:
            return False
        return True
         
# Leetcode: 941
# Rather messy solution to the problem. But it works.
# Time Complexity: O(n)
# Space Complexity: O(1) for some boolean flags and prev vaues (Which can be removed... if I think about it)
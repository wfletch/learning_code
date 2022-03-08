 class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed)%2 != 0:
            return []
        # Or we could...
        #   Go through the array, hash the counts.
        #   Iterate through the hashed counts and find the recipricols.. Decrement the count of each.
        # Add the values we used to the list
        k = collections.Counter(changed)
        # Cool, now we have the values hashed!
        # There are 2 possibilities for a number.
        # Either we need to find the doubleed value or the halved value.
        # If we find the doubled value. store this pick in our array
        # If we find the halved value. store the halved value in our array.
        # Check for double first.
        # Minus the count of each value
        orig = []
        b =  list(k.keys())
        b.sort()
        b.reverse()
        edit = False
        for val in b:
            while k[val] > 0: # Already been processed
                edit = False
                target = val
                # Look for Double
                double = target*2
                if k.get(double, -1) > 0:
                    # We have a double
                    k[double] -=1
                    k[target] -=1
                    orig.append(target)
                    edit = True
                else:
                    if target%2 != 0:
                        return []
                    half = target//2
                    if k.get(half, -1) > 0:
                        # We have a half
                        k[half] -=1
                        k[target] -=1
                        orig.append(half)
                        edit = True
                if edit == False:
                    return []
        return orig
            
 #LeetCode # 2007
        # Not super happy with the performance on this one. Will optimize Later!
        # Actualy it turned out ok: 91.39% Performance with 13% memory
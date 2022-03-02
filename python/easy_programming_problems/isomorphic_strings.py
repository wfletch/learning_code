class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Store a mapping of characters we have seen so far.
        s_hash = {}
        t_hash = {}
        # Linearly iterate through
        for i,v in enumerate(s):
            if v in s_hash:
                if t[i] == s_hash[v]:
                    continue
                else:
                    return False
            else:
                # Check if we have a collision on one of the values
                if t[i] in t_hash:
                    return False
                s_hash[v] = t[i]
                t_hash[t[i]] = v
        return True
            
             
#  LeetCode # 205
#  Time Complexity: O(n). 
#  Space Complexity: O(2n). Need to Store Additional Memory for both hashes
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Store a mapping of characters we have seen so far.
        s_hash = {}
        # Linearly iterate through
        for i,v in enumerate(s):
            if v in s_hash:
                if t[i] == s_hash[v]:
                    continue
                else:
                    return False
            else:
                # Check if we have a collision on one of the values
                for k in s_hash:
                    if s_hash[k] == t[i]:
                        return False
                s_hash[v] = t[i]
        return True
            
#  LeetCode # 205
#  Time Complexity: O(n^2). Need to iterate through the string and check hash for collision. Can be solved with an additional hash storing reverse mappings.
#  Space Complexity: O(n). Need to Store Additional
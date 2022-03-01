class Solution:
    def makeGood(self, s: str) -> str:
        l_pointer = 0
        r_pointer = 1
        while r_pointer < len(s):
            if s[l_pointer] == s[r_pointer]:
                # Same Letter. All is Good
                l_pointer+=1
                r_pointer+=1
            elif s[l_pointer] == s[r_pointer].upper() or s[l_pointer].upper() == s[r_pointer]:
                # Violation. Remove
                s = s[:l_pointer] + s[r_pointer+1:]
                l_pointer -=1
                r_pointer -=1
                if l_pointer < 0:
                    l_pointer+=1
                    r_pointer+=1
            else:
                l_pointer+=1
                r_pointer+=1
        return s
# LeetCode 1544
# Time Complexity O(n + k) where K is the number of edits we use. Also, a ton of time is being wasted on reformatting the string
# Space Complexity: O(1)
# How Would I optimize. I would keep the two pointer approach, but create an additional bit vector showing which elements are to be removed
# I would then adjust the 'next' value to get the next value which has not been added or checked in the bit vector
# This would significantly cut down the time spent re creating the string after each edit
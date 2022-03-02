class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Start from end countbackwards until you reach a space?
        word_count = 0
        k = len(s)-1
        # Get rid of trailing spaces:
        while s[k] == " ":
            k-=1
        while s[k] != " " and k > -1:
            word_count+=1
            k-=1
        return word_count
# LeetCode #: 58
# Time Complexity: O(1)
# Space Complexity: O(1) Just storing a count
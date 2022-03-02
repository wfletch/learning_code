class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # We are iterating through the lenght of the shortest word (Effectively)
        # In the beginning, we need to make sure all words start with the same n'th letter. n starts at 0
        # Repeat until we exceed a word length
        # Lazy: let's find the length of the smalles word first.
        # length = min([len(i) for i in strs]) # This is lazy. We can figure out the length in the loop. if we wanted!
        count = 0
        invalid = False
        for i in range(0,len(strs[0]),1):
            target = strs[0][i]
            for w in strs:
                if i == len(w):
                    invalid = True
                    break
                if w[i] == target:
                    continue
                else:
                    invalid = True
                    break
            if invalid:
                break
            count+=1
        if count == 0:
            return ""
        return strs[0][0:count]

# LeetCode # 14
# Time Complexity: O(n)
# Space Complexity: O(1)
# Some minor optimizations to how we find the max possible length of the prefixes
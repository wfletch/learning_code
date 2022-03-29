class Solution:
    def maxFreq(self, s, maxLetters, k, maxSize):
        # This is fucking amazing !!! - Credit to Lee!
        # So we actually only care about the minimum length. Anything larger will always appear the same or less
        # We create a slide of those and count the occurances
        count = Counter(s[i:i+k] for i in range(len(s) - k + 1))
        # Return the highgest count we can find provided our set  only contains unique values less than the required limit
        # List comprehension is amazing
        return max([count[w] for w in count if len(set(w)) <= maxLetters] + [0])
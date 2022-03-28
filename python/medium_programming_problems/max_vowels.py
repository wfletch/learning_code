class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # Sliding window count. Width of window is k
        cur_window = {}
        vowel_count = 0
        left = right = 0
        while right < len(s):
            # We need to add letters first
            cur_window[right]  = s[right]
            if right >= k-1:
                # Start checking
                vowel_count = max(vowel_count, sum([1  if i in 'aeiou' else 0 for i in list(cur_window.values())]))
                del cur_window[left]
                left+=1
            right +=1
        return vowel_count
        # While this took me 5 minutes to write! It is a bit slow. I think I can make it better!

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # Sliding window count. Width of window is k
        cur_window = {}
        max_vowel_count = vowel_count = 0
        left = right = 0
        while right < len(s):
            # We need to add letters first
            if s[right] in 'aeiou':
                vowel_count +=1
            if right >= k-1:
                # Start checking
                max_vowel_count = max(max_vowel_count, vowel_count)
                if s[left] in 'aeiou':
                    vowel_count -=1
                left+=1
            right +=1
        return max_vowel_count
        # Turns out...we don't need to keep track of the letters, just the vowel counts.
        # LC # 1456
        # Space: O(1)
        # Time: O(n)            
        
class Solution:
    def countVowels(self, word: str) -> int:
        def _countVowels(word=word):
            if len(word) == 1:
                if word in ['a','e','i','o','u']:
                    return 1
                else:
                    return 0
            else:
                count = 0
                l_word = len(word)
                for i,v in enumerate(word):
                    if v in ['a','e','i','o','u']:
                        count+=(l_word - i)
                return count + _countVowels(word[1:])
        return _countVowels()
                    
                    
        
        # LC # 2063
        # Time Complexity (N^2)
        # Space Complexity (N^2)
class Solution:
    def countVowels(self, word: str) -> int:
        def _countVowels(word=word):
            count = 0
            l_word = len(word)
            for i,v in enumerate(word):
                if v in ['a','e','i','o','u']:
                    count+=(l_word - i)
            max_allow = count
            # Go through the array again, but  minus the lenght of the value everytime you get a vowel
            for i,v in enumerate(word):
                if v in ['a','e','i','o','u']:
                    max_allow-=(l_word - i)
                count += max_allow
            return count
        return _countVowels()
                    
        # LC # 2063
        # Time O(2N)
        # Space O(1)


class Solution:
    def countVowels(self, word: str) -> int:
        return sum((i+1) * (len(word)-i) for i,v in enumerate(word) if v in 'aeiou')

    # LC # 2063
    # Time O(N)
    # Space O(1)
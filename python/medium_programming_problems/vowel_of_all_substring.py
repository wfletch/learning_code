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
                    
                    
        
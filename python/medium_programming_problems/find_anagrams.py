class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Naive Solution
        # Create a numbered vector of all the counts of each letter
        # At each point in the list, try and build until that count is 0
        # Repeat until we reach the end of the string
        letter_count = defaultdict(lambda: 0)
        cur_count = defaultdict(lambda: 0)
        solutions = []
        for i in p:
            letter_count[i] +=1
        print(letter_count)
        for i,v in enumerate(s):
            if i + len(p) > len(s):
                break
            found = True
            for j,u in enumerate(p):
                cur_count[s[i + j]] +=1
                if cur_count[s[i +j]] <= letter_count[s[i +j]] and letter_count[s[i +j]] > 0:
                    continue
                else:
                    found = False
                    break
            if found:
                solutions.append(i)
            cur_count = defaultdict(lambda: 0)
        return solutions
        # This is an N^2 Solution.

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # So m naive solution. sucks
        # Let's try cut down time complexity
        # first of all.
        solutions = []
        left, right = 0, len(p) -1
        p_hash = Counter(p)
        s_hash = Counter(s[left:right+1])
        if p_hash == s_hash:
            solutions.append(left)
        # Now we move from left to right. Removing and adding to s_hash.
        while right < len(s)-1:
            s_hash[s[left]]-=1
            left +=1
            right +=1
            s_hash[s[right]]+=1
            if p_hash == s_hash:
                solutions.append(left)
        return solutions
        # This is a Linear Solution, but damn that hash map

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_s,len_p = len(s), len(p)
        s_count, p_count = [0] * 26, [0] * 26
        #Populate initial state
        for i in p:
            p_count[ord(i) - ord('a')] +=1
        # Empty Solutions
        solutions = []
        for i in range(len(s)):
            # Iterate through the word, add letters where appropriate
            s_count[ord(s[i]) - ord('a')] +=1
            if i >= len_p:
                # Maximum lenght of the sliding window has been reached, let's remove
                # the value at the beginning of the window
                s_count[ord(s[i - len_p]) - ord('a')] -=1
            
            # Check for equality
            if p_count == s_count:
                solutions.append(i - len(p) + 1)
        return solutions
        
        # A solution using just a sliding window and an array
class Solution:
    # This is horribly, horribly slow. but it will work
    def generateParenthesis(self, n: int) -> List[str]:
        import itertools
        k = []
        for i in range(n):
            k.append('(')
            k.append(')')
        p = list(itertools.permutations(k))
        valid = []
        q = []
        for entry in p:
            not_valid = False
            for c in entry:
                if c == '(':
                    q.append(c)
                else:
                    if len(q) == 0:
                        not_valid = True
                        break
                    else:
                        q.pop()
            if not_valid:
                continue
            else:
                if "".join(entry) not in valid:
                    valid.append("".join(entry))    
        return valid
        # This is terribly inefficent 
class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        # So... how do we build expressions???
        # We have two vectors
        # we have numbers and we have operations
        # I guess we pick and try both
        # I guess we can back track.
        # We can also evaluate an expression in multiple ways
        # So, let's back track to build our expressions.
        # Once we have an expression, how would we process it?
        operations = ["+", "-", "*", "/"]
        expressions = []
        found_24 = False
        def _backtrack(path, cards):
            nonlocal found_24
            if found_24:
                return
            if len(cards) == 1:
                # We have one card left, add it!
                raw_expression = path + cards
                p_expressions = []
                p_expressions.append("".join([str(i) for i in raw_expression]))
                # This is a messy way to parenthesize, but it works.
                a = raw_expression.copy()
                a.insert(len(a), ")")
                a.insert(-4, "(")
                a.insert(-6, ")")
                a.insert(0, "(")
                p_expressions.append("".join([str(i) for i in a]))
                a = raw_expression.copy()
                a.insert(len(a), ")")
                a.insert(-2, "(")
                a.insert(5, ")")
                a.insert(0, "(")
                p_expressions.append("".join([str(i) for i in a]))
                a = raw_expression.copy()
                a.insert(len(a), ")")
                a.insert(2, "(")
                p_expressions.append("".join([str(i) for i in a]))
                a = raw_expression.copy()
                a.insert(-2, ")")
                a.insert(2, "(")
                p_expressions.append("".join([str(i) for i in a]))
                # p_expressions.append("".join([str(i) for i in a]))
                # expression = "".join([str(i) for i in path + cards])
                # How do we parenthesize it?
                try:
                    # Now... we have multiple ways to express this relation...
                    # Catalan Numbers.. 5 ways 4 terms.
                    for expression in p_expressions:
                        result = eval(expression)
                        if abs(result - 24) <= 0.001:
                            found_24 = True
                except:
                    pass
            else:
                # Ok, we backtrack
                for i,card in enumerate(cards):
                    path.append(cards[i])
                    for operation in operations:
                        path.append(operation)
                        # We cannot use the same card twice!
                        _backtrack(path, cards[0:i] + cards[i+1:])
                        path.pop()
                    path.pop()
        _backtrack([], cards)
        # Now we have all expressions. Let's
        return found_24
class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        right, left = a,b
        home = x
        # Brute force this bitch. Then add some history
        # I guess we can always jump forward and then jump backward, but we can't jump backward twice in a row
        # We know we are stuck in a cycle if we have been somewhere before.
        paths = []
        history = set()
        forbidden = set(forbidden)
        def _jump(x_loc, allow_back, num_jumps=0):
            if x_loc > 6000:
                # Beyond the game limits ?? ?
                return 
            if x_loc == home:
                # Cool, we are home
                paths.append(num_jumps)
                return
            if x_loc < 0:
                return
            if x_loc in history:
                return
            if allow_back:
                history.add(x_loc)
            # Let's jump forward
            if x_loc + right not in forbidden:
                _jump(x_loc + right, True, num_jumps+1)
            # Let's jump backwards
            if allow_back:
                if x_loc - left not in forbidden:
                    _jump(x_loc - left, False, num_jumps+1)
        _jump(0,True)
        if paths == []:
            return -1
        return min(paths)
        
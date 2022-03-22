class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        # We're going to create a list of values to start.
        # Then we are going to try build some numbers
        nums = [1,2,3,4,5,6,7,8,9]
        options = []
        def _buildNum(num, n=n, k=k):
            if len(num) == n:
                options.append(num)
            # We have two options
            else:
                # num is a str
                last_val = int(num[-1])
                # Try and add K
                if (last_val + k < 10) or k == 0:
                    _buildNum(num + str(last_val + k))
                if last_val - k > -1 and k != 0:
                    _buildNum(num + str(last_val - k))
        for i in nums:
            _buildNum(str(i))
        return options
        # LC 967
        # Time: O(2^n)
        # Space: O(2^n)
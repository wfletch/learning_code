class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_number = 1
        n-=1
        cur_num = 2
        # Could we do a seive?
        # We need to Recursively deivide down and see if the number comes to 1
        recur_hash = {1:1,3:1,5:1}
        
        while n > 0:
            if cur_num % 2 == 0:
                # This is divisible by 2
                if recur_hash.get(cur_num//2,None) != None:
                    recur_hash[cur_num] = 1
                    ugly_number = cur_num
                    n-=1
            elif cur_num % 3 == 0:
                if recur_hash.get(cur_num//3,None) != None:
                    recur_hash[cur_num] = 1
                    ugly_number = cur_num
                    n-=1
            elif cur_num % 5 == 0:
                if recur_hash.get(cur_num//5,None) != None:
                    recur_hash[cur_num] = 1
                    ugly_number = cur_num
                    n-=1
            cur_num+=1
        print(recur_hash)
        return ugly_number

        # LC: 264
        # This does not meet timelimit constraints. But it does seem to work for n < 700
        # Space: O(n... some math division here)
        # Time O(n) + a ton of divisions.
        
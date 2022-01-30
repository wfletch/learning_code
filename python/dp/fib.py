#!/usr/bin/python

import sys
# Fibonacci (Dynamic Programming)
# 2 Implementations using Dynamic Programming
# Note: There is a better way to compute this using Golden Ratio


def find_fib(k):
    # Space: O(N)
    # Time: O(N)
    if k  == 0:
        return 0
    if k <= 2:
        return 1
    # There if a further Optimization
    fib = {}
    for i in range(1, k+1):
        if i <= 2:
            fib[i] = 1
        else:
            fib[i] = fib[i-1] + fib[i-2]
    return fib[k]

def find_fib_optimal(k):
    # Space: O(1)
    # Time: O(N)
    fib = [1,1]
    if k == 0:
        return 0
    if k <= 2:
        return 1
    for i in range(3,k+1):
        temp = fib[0]
        fib[0] = fib[0] + fib[1]
        fib[1] = temp
    return fib[0]

if __name__ == "__main__":
    if len(sys.argv)  != 2:
        raise Exception("Please Specify K Value")
    k = int(sys.argv[1])
    assert find_fib(k) == find_fib_optimal(k), "Fibonacci Failed"
    print("Fibonacci Success")

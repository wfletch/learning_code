# Given a size (A), Print the following pattern
# A = 4
# 4 4 4 4 4 4 4
# 4 3 3 3 3 3 4
# 4 3 2 2 2 3 4
# 4 3 2 1 2 3 4
# 4 3 2 2 2 3 4
# 4 3 3 3 3 3 4
# 4 4 4 4 4 4 4

import sys
def solve(A):
    # Idea:
    # Have two Indexes: Left and Right
    # Add values to the locations of each index until the indeces overlap (or are the same)
    # Each iteration lower the max depth the number can go to
    # We can leverage the fact that the system is symettrical in the X and Y 'planes'
    # Therefore, we can solve row [x] as well as [max_dim - x] at the same time
    l = 0
    r = (A*2) - 2
    cur_dec = 0
    max_dec = 0
    res = [[-1 for x in range((A*2) -1)] for y in range((A*2) -1)]
    cur_row = 0
    while max_dec != A:
        while r - l >= 0:
            cur_val = A - cur_dec
            res[cur_row][l] = str(cur_val)
            res[cur_row][r] = str(cur_val)
            # Reflect around mid horizontal point
            res[(2*A) - 2 - cur_row][l] = str(cur_val)
            res[(2*A) - 2 - cur_row][r] = str(cur_val)
            if cur_dec != max_dec:
                cur_dec +=1 
            r-=1
            l+=1
        cur_row+=1
        max_dec+=1
        cur_dec=0
        l = 0
        r = (A*2) -2
    return (res)



if __name__ == '__main__':
    A = None
    try:
        A = int(input("Enter A Number to view a spiral!"))
    except Exception:
        print("{} Is Not a Number".format(A))
        sys.exit(-1)
    res = solve(A)
    for entry in res:
        print (" ".join(entry))

        


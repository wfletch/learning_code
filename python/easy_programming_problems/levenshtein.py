def levenshtein_distance(a,b):
    if len (b) == 0:
        return len(a)
    if len(a) == 0:
        return len(b)
    if a[0] == b[0]:
        return levenshtein_distance(a[1:], b[1:])
    else:
        return 1 + min(levenshtein_distance(a[1:],b), levenshtein_distance(a,b[1:]),levenshtein_distance(a[1:],b[1:]))

def dp_levenshtein_distance(s,t):
    # TODO: Faulty Code. Fix!
    m = len(s)+1
    n = len(t)+1
    d = [[0 for i in range(0,m+1,1)] for k in range(0,n+1,1)]
    for i in range(0,m+1,1):
        d[0][i] = i
    for j in range(0,n+1,1):
        d[j][0] = j
    print(d)
    for j in range(1,n,1):
        for i in range(1,m,1):
            if s[i] == t[j]:
                sub_cost = 0
            else:
                sub_cost = 1
            d[i][j] = min(d[i-1][j] + 1,
                        d[i][j-1] + 1,
                        d[i-1][j-1] + sub_cost)
    print(d)
    return d[m][n]
if __name__ == "__main__":
    assert levenshtein_distance('cat', 'hat') == 1
    print(dp_levenshtein_distance("Saturday","Sunday"))
    # This is fucking inefficent. But will work.
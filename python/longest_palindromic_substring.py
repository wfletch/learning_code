def lpss(x, i, j):
    memo = {}
    if i == j:
        return 1
    elif x[i] == x[j]:
        return 2
    else:
        return max(lpss(x,i+1,j), lpss(x, i,j+1))

if __name__ == "__main__":
    print("Work In Progress")

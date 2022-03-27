def substrings(s):
    return [s[i:j] for i in range(len(s)) for j in range(i+1, len(s) + 1)]

if __name__ == "__main__":
    print (substrings("Warren"))
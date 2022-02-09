def isUnique(a):
    # Space: O(n)
    # Time: O(n)
    # How Would I optimize?
    # Time:     Cannot - You got to iterate through each element at least once
    # Space:    Can do a nested loop and search for other occurances of the character O(n^2)
    #           Can Sort and see if adjacent characters are the same O(nlogn) + O(n)
    letter_count = {}
    for l in a:
        if letter_count.get(l,False):
            return False
        else:
            letter_count[l] = True
    return True

if __name__ == "__main__":
    print(isUnique("abcdef"))
    print(isUnique("abcdefa"))
    print(isUnique("abcdefghijklmnopqrstuvwxyz"))

def isUnique(a):
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

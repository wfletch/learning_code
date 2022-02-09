from collections import defaultdict
def checkPermutation(a,b):
    # Check if String A is a permutaiton of String B
    # End Early: Strings are not the same length
    # Space: O(2n)
    # Time: O(2n)
    # Optimize:
    #           Time:   Not Possible
    #           Space:  I theroize I can sum special values(Ord(a[i]) * Some Prime).
    #                   This would require constant time.
    if len(a) != len(b):
        return False
    # IDEA: Count the number of letters in a hash and make sure all counts are 0 by the end
    letter_mem = defaultdict(lambda: 0)
    for i in range(len(a)):
        letter_mem[a[i]] +=1
        letter_mem[b[i]] -=1
    for k in  letter_mem.keys():
        if letter_mem[k] != 0:
            return False
        else:
            return True

if __name__ == "__main__":
    print(checkPermutation("Warren", "Fletcher"))
    print(checkPermutation("Julia", "Jiaul"))
    print(checkPermutation("abcdefghijklmnop", "acbdefghikjlmnpo"))

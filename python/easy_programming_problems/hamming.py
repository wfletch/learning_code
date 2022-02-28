def hamming(a,b):
    if len(a) != len(b):
        return -1
    # Take two strings, calculate the number of different characters
    count = 0
    for i in a:
        for j in b:
            if i != j:
                count+=1
        break
    return count


if __name__ == "__main__":
    assert hamming("warren","warjen") == 1
    assert hamming("warren","waren") == -1
    assert hamming("warren","warjeN") == 2 # Capitals are different!
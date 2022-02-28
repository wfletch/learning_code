def levenshtein_distance(a,b):
    if len (b) == 0:
        return len(a)
    if len(a) == 0:
        return len(b)
    if a[0] == b[0]:
        return levenshtein_distance(a[1:], b[1:])
    else:
        return 1 + min(levenshtein_distance(a[1:],b), levenshtein_distance(a,b[1:]),levenshtein_distance(a[1:],b[1:]))

if __name__ == "__main__":
    assert levenshtein_distance('cat', 'hat') == 1
    # This is fucking inefficent. But will work.
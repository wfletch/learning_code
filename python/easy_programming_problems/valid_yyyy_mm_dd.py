def valid_yyyy_mm_dd(date):
    yyyy,mm,dd = date.split('-')
    # Trivial Evaulation
    if int(yyyy) < 0:
        return False
    if int(mm) > 13 or int(mm) < 1:
        return False
    if int(dd) > 31 or int(mm) < 1:
        return False
    # Check if Valud 30-day Date
    if int(mm) in [4,6,9,11] and int(dd) <31:
        return True
    if int(mm) in [1,3,5,7,8,10,12] and int(dd) < 32:
        return True
    if (int(yyyy) % 4 == 0 and int(dd) < 30):
        return True
    if int(dd) < 29:
        return True
    return False

if __name__ == "__main__":
    # TODO: Make this a proper test framework
    assert valid_yyyy_mm_dd("1994-07-23") == True
    assert valid_yyyy_mm_dd("1994-07-32") == False 
    assert valid_yyyy_mm_dd("2000-02-29") == True
    assert valid_yyyy_mm_dd("2001-02-29") == False
    assert valid_yyyy_mm_dd("1994-01-35") == False
    print("Passes Tests")

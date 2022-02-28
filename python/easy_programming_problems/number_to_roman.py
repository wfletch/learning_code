def number_to_roman(number):
    # We are going to have a limit on the number we can convert
    if number > 3999 or number < 1:
        return False
    roman_num = [] # This could technically be a fixed length array. 
    # Idea: We have a special case for thousands (There is not Mid Roman Number)
    thousands = number // 1000
    if thousands > 0:
        roman_num.append(thousands * "M")
    number -= (thousands * 10**3)
    # Now, we have upper values and mid values and low values for each factor of 10
    # Exmple: For thousands we have M (1000) upper and D (500) middle and C(100) low
    # If, after modulation, we have a value of 9 we take our Upper and subtract 1 Lower
    # If, after modulation, we have a value between 5 and 8 (inclusive), we take our Middle and add value - 5 of Lower
    # If, after modulation, we have a value of 4, we take our Middle and subtract 1 Lower
    # If, after modulation, we have a value between 1 and 3 (inclusive). We add value of Lower
    # After each round we shift our upper,middle, and lower 'down' by 2
    r_numerals = ["I", "V", "X", "L", "C", "D", "M"]
    upper_i = len(r_numerals) -1
    middle_i = upper_i - 1
    lower_i = middle_i - 1
    for i in range(2,-1,-1):
        # We only have 3 orders of magnitude
        decrement = 10**i
        remainder = number // decrement
        upper = r_numerals[upper_i]
        middle = r_numerals[middle_i]
        lower = r_numerals[lower_i]
        if remainder == 9:
            roman_num.append( 1 * lower + 1 * upper) 
        elif remainder > 4:
            roman_num.append(1 * middle + (remainder - 5) * lower) 
        elif remainder == 4:
            roman_num.append( 1 * lower + 1 * middle)
        else:
            roman_num.append(remainder * lower)
        number -= decrement *remainder
        upper_i -= 2 
        middle_i -= 2 
        lower_i -= 2
    return "".join(roman_num)

if __name__ == "__main__":
    print(number_to_roman(3999))
    print(number_to_roman(4))
    print(number_to_roman(45))
    print(number_to_roman(456))
    print(number_to_roman(1234))
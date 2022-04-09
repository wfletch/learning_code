

def range_sum(number):
    number_str = str(number)
    answers = []
    for i in range(0, len(number_str),1):
        lower_bound = max(i - int(number_str[i]),0)
        upper_bound = min(i + int(number_str[i]), len(number_str)-1)
        cur_sum = 0
        for j in range(lower_bound, upper_bound+1,1):
            cur_sum += int(number_str[j])
        answers.append(cur_sum)
    return answers
print(range_sum(11122322111))


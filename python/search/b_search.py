import sys
#TODO: recursive Interation
def recursive_search(sorted_list, element, lower_index=-1, upper_index=0):
    pass
def b_search(sorted_list, element):
    # Process
    # Take the middle element(predicate) and compare it to the element we are looking for
    # If element == predicate. Return that we have found it
    # If element > predicate. Research with lower_bound = middle_point. Upper_bound remains unchanged
    # If element < predicate. Reserach with upper_bound = middle_point. Lower bound remains unchanged
    # If gap between upper index and lower index <= 1: Return False (We have not found the element in the list)
    
    #Linear Solution


    found_element = False
    lower_index = 0
    upper_index = len(sorted_list) # Because we devide down, we need to 'reach over' the last element in a list
    iter_count = 1
    while (upper_index - lower_index) > -1:
        mid_point = (upper_index - lower_index)//2 + lower_index #Got to love integer div
        predicate = sorted_list[mid_point]
        if element == predicate:
            found_element = True
            break
        elif element > predicate:
            lower_index = mid_point
        else:
            upper_index = mid_point
        iter_count+=1
        if iter_count >= 100:
            return False
    if found_element:
        return iter_count
    else:
        return False

if __name__ == '__main__':
    search_list = [i for i in range(20000)]
    for i in range(2):
        print (b_search(search_list,i))




def water_problem(height, water_level):
    if height == []:
        return 0
    # Ok, we are going to sweep through and track the 'maximum' amount of water we could hold so far
    # This is defined by the beginning block height OR the water_level (Which ever is smaller)
    # Each segment is deliminated by:
    #   Peak higher than the water level/block_height
    # If during the pass we find a -1 height. We know we have a sink
    #   This just means the current path has zero contribution to the total water we can store
    # [0, 1, 0, 4, 2, 5, 3, -1, 2]
    # TODO: Keep track of highest point as we go along. It is possible to have sub heights
    l_pointer = 0
    r_pointer = 0
    cur_peak = water_level
    cur_bucket_water = 0
    total_water = 0
    invalid_bucket = False
    while r_pointer < len(height):
        print(total_water)
        if height[r_pointer] <= cur_peak:
            cur_bucket_water += water_level - height[r_pointer]
        if height[r_pointer] > cur_peak or r_pointer == len(height)-1:
            # This Bucket has ended!
            # If it is valid, tally up everything and move on
            if not invalid_bucket:
                total_water += cur_bucket_water
                l_pointer = r_pointer
                invalid_bucket = False
                if l_pointer + 1 < len(height):
                    cur_peak = water_level if water_level >= height[l_pointer+1] else height[l_pointer+1]
                l_pointer +=1
                r_pointer +=1
            else:
                l_pointer = r_pointer
                l_pointer+=1
                r_pointer+=1
            continue
        if height[r_pointer] == -1:
            invalid_bucket = True
        r_pointer +=1
    return total_water 

if __name__ == "__main__":
    print(water_problem([0, 1, 0, 4, 2, 5, 3, -1, 2], 4))

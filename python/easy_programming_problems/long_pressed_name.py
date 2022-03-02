class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        # Let's iterate thorugh the array and do basic counting of the values we find
        # This is very overkill for the problem. A Better solution would involve pointers and counting forwards
        cur_name_letter_count = 0
        cur_name_letter = name[0]
        name_count_list = []
        for i in name:
            if i == cur_name_letter:
                cur_name_letter_count +=1
            else:
                name_count_list.append(str(cur_name_letter_count) + cur_name_letter)
                cur_name_letter_count = 1
                cur_name_letter = i
        name_count_list.append(str(cur_name_letter_count) + cur_name_letter)
        
        cur_name_letter_count = 0
        cur_name_letter = typed[0]
        typed_count_list = []
        for i in typed:
            if i == cur_name_letter:
                cur_name_letter_count +=1
            else:
                typed_count_list.append(str(cur_name_letter_count) + cur_name_letter)
                cur_name_letter_count = 1
                cur_name_letter = i
        typed_count_list.append(str(cur_name_letter_count) + cur_name_letter)

        # A better way to store this would be with two arrays. One of letter and one of count. No Splitting Needed
        if len(name_count_list) != len(typed_count_list):
            return False
        for i in range(0,len(name_count_list),1):
            if name_count_list[i][-1:] != typed_count_list[i][-1:]:
                # Letter is Different
                return False
            if int(name_count_list[i][:-1]) > int(typed_count_list[i][:-1]):
                return False
        return True

# LeetCode:  925
# This is realy Overkill.
# I should rewrite this using two pointers.
# Time Complexity: O(n) + a ton of appends and splits
# Space Complexity: O(n)
# 3/10 Would Do Again.

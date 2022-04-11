class Solution:
    def compress(self, chars: List[str]) -> int:
        # Store this result in the input array... ok, nice twist
        # We can edit in place.
        pos_pointer = 0
        cur_pointer = 1
        # Two pointer technique, Everytime we reach an end, we fill in the value in the pos_pointer.
        # Once cur_pointer reached end, we can return the char up to that point as well as ther value of the array
        #Let's do this
        current_value = chars[0]
        current_count = 1
        while cur_pointer < len(chars):
            contender = chars[cur_pointer]
            if contender == current_value:
                # Continue counting
                current_count+=1
            else:
                # Ok, we need to update our position!
                chars[pos_pointer] = current_value
                pos_pointer+=1
                if current_count != 1:
                    # We can append the count as well:
                    for i in str(current_count):
                        chars[pos_pointer] = i
                        pos_pointer+=1
                # Ok, we are now past the previous
                current_value = contender
                current_count = 1
            cur_pointer+=1
        # When we reach the end, we still will need to check
        chars[pos_pointer] = current_value
        pos_pointer+=1
        if current_count != 1:
            # We can append the count as well:
            for i in str(current_count):
                chars[pos_pointer] = i
                pos_pointer+=1
        # Now we should be done
        return (pos_pointer)
        # LC # 443
        # Time: O(n)
        # Space: O(1)
        # Flawless!
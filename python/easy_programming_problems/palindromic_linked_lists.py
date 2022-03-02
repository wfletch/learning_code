# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head.next == None:
            return True
        if head.next.next == None:
            return head.val == head.next.val
        if head.next.next.next == None:
            return head.val == head.next.next.val
        b_pointer = None
        c_pointer = head
        f_pointer = head
        r_pointer = head
        found_even = False
        while r_pointer.next != None:
            if r_pointer.next.next == None:
                # Even Case of Nodes!
                found_even = True
                c_pointer = copy.deepcopy(f_pointer)
                c_pointer.next = b_pointer
                f_pointer = f_pointer.next
                break
            else:
                # Normal Case
                r_pointer = r_pointer.next.next
                f_pointer = f_pointer.next
                c_pointer.next = copy.deepcopy(b_pointer)
                b_pointer = c_pointer
                c_pointer = copy.deepcopy(f_pointer)
        if found_even:
            b_pointer = c_pointer
            f_pointer = f_pointer
        else:    
            b_pointer = b_pointer
            f_pointer = f_pointer.next
        while b_pointer != None and f_pointer != None:
            if f_pointer.val != b_pointer.val:
                return False
            f_pointer = f_pointer.next
            b_pointer = b_pointer.next
        return True
# Leetcode #: 234
# Note. This... Exceeds the run time bound of the exam system but seems to pass testing.
# I would probably not have used a language like python to solve this. I would have preferred a pointer language (Like Go)
# Space Complexity O(1): At least in theory. Python's Deepcopies are getting in my way
# Time Complexity O(n)
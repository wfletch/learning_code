# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Two Pointers. Iterate through, Keep the gap n values across. When you get to the end remove this node
        # Hell, you can even do n-1 and lookahead to delete that value.
        # Not Hard, just time consuming.
        runner = head
        previous = None
        #The goal here is to remove the node ahead of previous when runner.next == None
        # 1 2 3 4 5, Remove 2nd node.
        # - - P - R
        # We need to take care with edge caes
        # EC1: Delete last node. Not really a problem
        # EC2: Delete first node. Little bit more tricky
        if head.next == None:
            return ListNode("")
        runner = head
        previous = head
        while runner.next != None:
            if n != 0:
                runner = runner.next
                n-=1
            else:
                runner = runner.next
                previous = previous.next      
        if n!= 0:
            # We need to remove the first node
            head = head.next
            return head
        if head.next == runner:
            head.next = None
            return head
        
        previous.next = previous.next.next
        return head
        
        # LC: 19
        # Ugh, this is painful. So many annoying edge cases to deal with
        # Time Complexity O(n)
        # Space Complexity O(1)
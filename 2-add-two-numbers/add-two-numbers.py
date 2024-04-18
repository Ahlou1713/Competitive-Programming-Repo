# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Check if either list is empty
        if not l1:
            return l2
        if not l2:
            return l1
        
        # Initialize pointers
        dummy = ListNode(-1)  # Dummy node
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            curr.next = ListNode(total % 10)
            
            # Move pointers forward
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            curr = curr.next
        
        return dummy.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Reverse the input linked lists
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)
        
        dummy = ListNode(-1)
        curr = dummy
        carry = 0
        
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            curr.next = ListNode(total % 10)
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            curr = curr.next
        
        # Reverse the result linked list
        result = self.reverseList(dummy.next)
        
        return result
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = None
        curr = head
        
        while curr:
            next_node = curr.next
            curr.next = new_head
            new_head = curr
            curr = next_node
        
        return new_head



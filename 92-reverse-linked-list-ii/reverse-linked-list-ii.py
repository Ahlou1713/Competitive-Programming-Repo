# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        new_head = ListNode(0) #dummy node
        new_head.next = head
        prev = new_head
        for _ in range(left - 1):
            prev = prev.next
        
        curr = prev.next
        next_node = None
        
        for _ in range(right - left):
            next_node = curr.next
            
            # Perform the reversing!
            curr.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node
    
        return new_head.next #skip the dummy node
        
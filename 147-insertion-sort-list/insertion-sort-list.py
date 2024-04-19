# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()

        dummy2 = ListNode()
        dummy2.next = head
        curr = dummy2
        while curr.next:
            prev = dummy
            while prev.next and curr.next.val > prev.next.val:
                prev = prev.next
            
            # Placing the element
            next_node = prev.next
            prev.next = curr.next
            another_next_node = curr.next.next
            curr.next.next = next_node
            curr.next = another_next_node

        return dummy.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head

        # Calculate the length of the linked list
        length = 1
        curr = head
        while curr.next:
            curr = curr.next
            length += 1
        curr.next = head # forming a cycle

        k = k % length # This is the actual rotation 'metric'

        for _ in range(length - k - 1):
            head = head.next

        new_head = head.next
        head.next = None

        return new_head 
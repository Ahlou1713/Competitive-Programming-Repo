# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        first_occurrence = {}
        curr = head

        while curr:
            if curr.val not in first_occurrence:
                first_occurrence[curr.val] = curr
            curr = curr.next

        curr = head
        prev = None

        while curr:
            if first_occurrence[curr.val] != curr:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        return head

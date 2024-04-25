# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dic = {}
        curr = head
        prev = None

        # Count occurrences of each value
        while curr:
            if curr.val in dic:
                dic[curr.val] += 1
            else:
                dic[curr.val] = 1
            prev = curr
            curr = curr.next

        curr = head
        prev = None

        # Remove duplicates
        while curr:
            if dic[curr.val] > 1:
                if prev:
                    prev.next = curr.next
                else:
                    head = curr.next  
            else:
                prev = curr
            curr = curr.next
        
        return head

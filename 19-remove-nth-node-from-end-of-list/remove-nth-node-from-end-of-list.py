# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # k = 0
        # curr = head
        # while curr:
        #     k += 1
        #     curr = curr.next

        dummy = ListNode(-1)
        dummy.next = head
        head = dummy
        # head = dummy
        # for i in range(k-n):
        #     head = head.next
        # head.next = head.next.next if head.next else None

        

        fast = head
        slow = head

        for _ in range(n):
            fast = fast.next

        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next if slow.next else None

        return dummy.next 


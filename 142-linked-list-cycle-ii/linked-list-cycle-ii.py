# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head

        meeting_point = None
        
        # phase 1
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            # phase 2
            if fast == slow:
                meeting_point = slow
                break

        # If there's no cycle, return None
        if meeting_point is None:
            return None

        # phase 2: find the start of the cycle
        ptr1 = head
        ptr2 = meeting_point
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        return ptr1

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        # Function to reverse a linked list
        def reverseLinkedList(node):
            prev = None
            while node:
                next_node = node.next
                node.next = prev
                prev = node
                node = next_node
            return prev

        # Function to find the middle of the linked list without using slow and fast pointers
        def findMiddle(node):
            count = 0
            curr = node
            while curr:
                count += 1
                curr = curr.next
            mid = count // 2
            for _ in range(mid):
                node = node.next
            return node

        # Find the middle of the linked list
        mid = findMiddle(head)

        # Reverse the second half of the linked list
        second_half = reverseLinkedList(mid)

        # Compare the first half with the reversed second half
        while second_half:
            if head.val != second_half.val:
                return False
            head = head.next
            second_half = second_half.next

        return True

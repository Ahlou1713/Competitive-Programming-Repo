class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = Node(0)
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        else:
            curr = self.head.next
            i = 0
            while i < index:
                curr = curr.next
                i+=1

            return curr.value

    def addAtHead(self, val: int) -> None:
        head = self.head.next
        self.head.next = Node(val)
        self.head.next.next = head
        self.size += 1

        # self.head.next = Node(val, self.head.next) <- this is better!

    def addAtTail(self, val: int) -> None:
        curr = self.head
        while curr.next != None:
            curr = curr.next

        curr.next = Node(val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return 
        curr = self.head
        i = 0
        while i < index:
            curr = curr.next
            i+=1
        curr.next = Node(val, curr.next)
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return 
        curr = self.head
        i = 0
        while i < index:
            curr = curr.next
            i+=1
        curr.next = curr.next.next
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
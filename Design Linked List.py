
class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        if self.head is None: return -1
        if index == 0:
            return self.head.val
        temp = self.head
        for _ in range(index):
            if temp.next == None:
                return -1
            temp = temp.next
        if temp : return temp.val
        return -1
    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node


    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.head = Node(val)
            return
        prev = self.head
        while prev.next:
            prev = prev.next
        prev.next = Node(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            new_node = Node(val)
            new_node.next = self.head
            self.head = new_node
            return
        temp = self.head
        for _ in range(index - 1):
            if not temp: return -1
            if temp.next == None:
                return -1
            temp = temp.next
        new_node = Node(val)
        new_node.next = temp.next if temp else None
        if temp: temp.next = new_node


    def deleteAtIndex(self, index: int) -> None:
        temp = self.head
        if index == 0 and self.head:
            self.head = self.head.next
            return
        elif not self.head:
            return None
        for _ in range(index - 1):
            if not temp: return None
            if temp.next is None:
                return None
            temp = temp.next
        temp.next = temp.next.next if temp.next else None
        return None


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()

# param_1 = obj.get(index)
# obj.addAtHead(7)
# obj.addAtHead(2)
# obj.addAtHead(1)
# pass
# obj.addAtTail(3)
# # pass
# obj.addAtIndex(3,0)
# pass
# obj.get(1)
# pass
# obj.deleteAtIndex(2)
# obj.addAtHead(6)
# pass
obj.addAtTail(1)
obj.get(4)

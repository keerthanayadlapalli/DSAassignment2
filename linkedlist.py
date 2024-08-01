class Node:
    def _init_(self, data):
        self.val = data
        self.next = None

class MyLinkedList:
    def _init_(self):
        self.head = None

    def length(self) -> int:
        count = 0
        temp = self.head
        while temp is not None:
            count += 1
            temp = temp.next
        return count

    def get(self, index: int) -> int:
        len_list = self.length()
        if self.head is None or index >= len_list:
            return -1
        count = 0
        temp = self.head
        while count < index:
            temp = temp.next
            count += 1
        return temp.val if temp is not None else -1

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        new_node = Node(val)
        if index == 0:
            self.addAtHead(val)
        else:
            count = 0
            temp = self.head
            while temp is not None and count < index - 1:
                temp = temp.next
                count += 1
            if temp is None:
                return
            new_node.next = temp.next
            temp.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        if self.head is None:
            return
        if index == 0:
            temp = self.head
            self.head = self.head.next
            del temp
        else:
            count = 0
            temp = self.head
            while count < index - 1:
                temp = temp.next
                count += 1
            if temp is None or temp.next is None:
                return
            to_delete = temp.next
            temp.next = temp.next.next
            del to_delete
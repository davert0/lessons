class Node:
    def __init__(self, v):
        self.value = v
        self.next = None
        self.prev = None


class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        res = []
        node = self.head
        while node is not None:
            if node.value == val:
                res.append(node)
            node = node.next
        return res

    def delete(self, val, all=False):
        if self.head is None:
            return None

        while self.head.value == val:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
                return
            if not all:
                return

        node = self.head
        if self.head.prev is not None:
            self.head.prev = None
        while node is not None:
            if node.value == val:
                node.prev.next = node.next
                if node.prev.next is None:
                    self.tail = node.prev
                else:
                    node.next.prev = node.prev
                if not all:
                    break
            node = node.next
        return None

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        res = 0
        node = self.head
        while node is not None:
            res += 1
            node = node.next
        return res

    def insert(self, afterNode, newNode):
        if self.tail is None:
            self.tail = newNode
        if afterNode is None and self.len() == 0:
            buff = self.head
            self.head = newNode
            self.head.next = buff
            return
        elif afterNode is None:
            self.add_in_tail(newNode)
            return
        node = self.head
        while node is not None:
            if node == afterNode:
                if node.next is not None:
                    node.next.prev = newNode
                
                newNode.next = node.next
                node.next = newNode
                newNode.prev = node
                if newNode.next is None:
                    self.tail = newNode
                return
            node = node.next

    def add_in_head(self, newNode):
        if self.head is None:
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
        self.head = newNode

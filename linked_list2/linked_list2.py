class Node:
    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

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

        prev = self.head
        node = self.head
        while node is not None:
            if node.value == val:
                if all:
                    prev.next = node.next if node.next is not None and node.next.value != val else prev.next
                    node = node.next
                    if node is None:
                        prev.next = None
                        self.tail = prev
                    continue
                else:
                    prev.next = node.next
                if prev.next is None:
                    self.tail = prev
                if not all:
                    return

            prev = node 
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
        if afterNode is None:
            buff = self.head
            self.head = newNode
            self.head.next = buff
            return
        node = self.head
        while node is not None:
            if node == afterNode:
                buff = node.next
                node.next = newNode
                newNode.next = buff
                if newNode.next is None:
                    self.tail = newNode
                return
            node = node.next

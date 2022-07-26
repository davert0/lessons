class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        if v1 < v2:
            return -1 if self.__ascending else 1
        if v1 == v2:
            return 0
        return 1 if self.__ascending else -1

    def add(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        node = self.head
        while node:
 
            if not node.next and self.compare(node.value, new_node.value) < 0:
                
                node.next = new_node
                new_node.prev = node
                self.tail = new_node
                return
            if not node.next and self.compare(node.value, new_node.value) >= 0:
                node.prev = new_node
                self.tail = node
                new_node.next = node
                if self.head == node:
                    self.head = new_node
                return

            if (
                node.next
                and self.compare(node.value, new_node.value) < 0
                and self.compare(node.next.value, new_node.value) >= 0
            ):
                node.next.prev = new_node
                new_node.next = node.next
                node.next = new_node
                new_node.prev = node
                return

            if self.compare(node.value, new_node.value) >= 0:
                node.prev = new_node
                new_node.next = node
                self.head = new_node
                return

            node = node.next

    def find(self, val):
        node = self.head
        while node:
            if node.value == val:
                return node
            if self.__ascending and node.value > val:
                return None
            if not self.__ascending and node.value < val:
                return None
            node = node.next
        return None

    def delete(self, val):
        if not self.head:
            return None

        if self.head.value == val:
            self.head = self.head.next
            if not self.head:
                self.tail = None
                return
            self.head.prev = None
            return

        node = self.head
        if self.head.prev:
            self.head.prev = None

        while node:
            if node.value == val and not node.next:
                    self.tail = node.prev
                    node.prev.next = None
                    return
            if node.value == val:
                node.prev.next = node.next
                node.next.prev = node.prev
                return
            node = node.next
        return None

    def clean(self, asc):
        self.__ascending = asc
        self.head = None
        self.tail = None

    def len(self):
        res = 0
        node = self.head
        while node:
            res += 1
            node = node.next
        return res

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r


class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)
        self.__ascending = asc

    def compare(self, v1, v2):
        v1, v2 = str(v1).strip(), str(v2).strip()
        if v1 < v2:
            return -1 if self.__ascending else 1
        if v1 == v2:
            return 0
        return 1 if self.__ascending else -1

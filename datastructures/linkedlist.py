class Node(object):

    def __init__(self, value, *args, **kwargs):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList(object):

    def __init__(self, *args, **kwargs):
        self.head = None

    def __repr__(self):
        node = self.head
        if not node:
            return None

        values = [str(node.value)]
        while node.next:
            node = node.next
            values.append(str(node.value))

        return ' '.join(values)

    def size(self):
        node = self.front()
        if not node:
            return 0

        length = 1

        while node.next:
            length += 1
            node = node.next

        return length

    def empty(self):
        return self.head is None

    def value_at(self, index):
        node = self.front()
        if not node:
            return

        for i in range(index):
            if node.next is None:
                raise KeyError("Index does not exist.")

            node = node.next

        return node.value

    def push_front(self, value):
        node = self.front()
        self.head = Node(value)
        self.head.next = node

    def pop_front(self):
        node = self.front()
        self.head = node.next
        value = node.value
        del node
        return value

    def push_back(self, value):
        node = self.back()
        if not node:
            self.head = Node(value)
            return

        node.next = Node(value)

    def pop_back(self):
        prev = None
        node = self.head
        if not node:
            return

        while node.next:
            prev = node
            node = node.next

        prev.next = None
        value = node.value
        del node

        return value

    def front(self):
        return self.head

    def back(self):
        if self.head is None:
            return None

        node = self.head
        while node.next:
            node = node.next

        return node

    def insert(self, index, value):
        node = self.front()
        if not node:
            return

        for i in range(index):
            if node.next is None:
                raise KeyError("Index does not exist.")

            node = node.next

        new_node = Node(value)
        new_node.next = node.next
        node.next = new_node

    def erase(self, index):
        node = self.front()
        prev = None

        if not node:
            return

        for _ in range(index):
            if node.next is None:
                raise KeyError("Index does not exist.")

            prev = node
            node = node.next

        if prev:
            prev.next = node.next
        else:
            self.head = node.next

        del node

    def value_n_from_end(self, n):
        p1 = self.front()
        p2 = self.front()

        length = 0
        while p2.next:
            p2 = p2.next
            length += 1

        for _ in range(length-n):
            p1 = p1.next

        return p1.value

    def reverse(self):
        prev = None
        nextNode = None
        node = self.head
        if not node:
            return

        while node:
            nextNode = node.next
            node.next = prev
            prev = node
            node = nextNode

        self.head = prev

    def remove_value(self, value):
        node = self.front()
        index = 0
        if node == value:
            self.erase(index)

        while node.next:
            node = node.next
            index += 1

            if node == value:
                self.erase(index)


lst = LinkedList()
lst.push_back(1)
lst.push_back(2)
lst.push_back(3)

assert (lst.size() == 3), "%s is not 3" % lst.size()

lst.reverse()
assert (str(lst) == "3 2 1"), "%s is not list reversed" % lst

lst.erase(1)

assert (str(lst) == "3 1"), "%s index 0 is not removed." % lst

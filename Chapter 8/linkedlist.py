class Node():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return str(self.__dict__)


class LinkedList():
    def __init__(self, value):
        self.head = Node(value, next=None)
        self.tail = self.head
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def insert(self, index, value):
        new_node = Node(value)
        if index <= 0:
            self.prepend(value)
            return self
        # pitfall: index has to be same as current index (not len-1)
        # Since we are going to add a new node, we have to count the new one, too
        if index >= self.length:
            self.append(value)
            return self
        foregoing_node = self.traverse_to_index(index-1)
        following_node = self.traverse_to_index(index)
        foregoing_node.next = new_node
        new_node.next = following_node
        self.length += 1

    def traverse_to_index(self, index):
        current_node = self.head
        for i in range(0, index):
            current_node = current_node.next
        return current_node

    def print_list(self):
        arr = []
        node = self.head
        while node.next:
            arr.append(node.value)
            node = node.next
            if not node.next:
                arr.append(node.value)
        print(arr)

    def __repr__(self):
        return str(self.__dict__)


if __name__ == "__main__":
    my_linked_list = LinkedList(25)
    my_linked_list.append(10)
    my_linked_list.append(13)
    my_linked_list.prepend(150)
    my_linked_list.append(17)
    my_linked_list.prepend(15)
    my_linked_list.print_list()
    my_linked_list.insert(1, 100)
    my_linked_list.print_list()
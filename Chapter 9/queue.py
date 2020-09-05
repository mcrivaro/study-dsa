class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.__dict__)


class Queue():
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        if self.first:
            print(self.first.value)
            return self.first.value

    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
        else:
            self.last.next = new_node
        self.last = new_node
        self.length += 1
        return new_node

    def dequeue(self):
        if not self.first:
            return None
        if self.first == self.last:
            self.last = None
        removed_val = self.first
        self.first = self.first.next
        self.length -= 1
        return removed_val

    def __repr__(self):
        return str(self.__dict__)


if __name__ == "__main__":
    my_queue = Queue()
    my_queue.enqueue('Joy')
    my_queue.enqueue('Matt')
    my_queue.enqueue('Pavel')
    my_queue.enqueue('Samir')
    my_queue.peek()
    my_queue.dequeue()
    my_queue.dequeue()
    my_queue.peek()
    my_queue.dequeue()
    my_queue.peek()
    my_queue.dequeue()
    my_queue.peek()
    print(my_queue)

class Node():
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return str(self.__dict__)


class Stack():
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def push(self, value):
        new_node = Node(value=value)
        if self.length < 1:
            self.bottom = new_node
        new_node.next = self.top
        self.top = new_node
        self.length += 1

    def pop(self):
        if self.length is 0:
            return None
        old_top = self.top
        self.top = self.top.next
        self.length -= 1
        if self.length is 0:
            self.bottom = None
        return old_top.value

    def peek(self):
        return self.top.value

    def __repr__(self):
        return str(self.__dict__)


if __name__ == "__main__":
    my_stack = Stack()
    my_stack.push('Amazon.com')
    my_stack.push('Google.com')
    my_stack.push('Youtube.com')
    print(my_stack.pop())
    print(my_stack.pop())
    print(my_stack.peek())
    print(my_stack)

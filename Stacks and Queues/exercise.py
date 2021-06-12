# implement a queue using stacks

class MyQueue(object):
    def __init__(self):
        self.stack1 = [] # stack order, use to push to queue
        self.stack2 = [] # queue order, use to pop from queue
        self.length = 0

    def push(self, x):
        self.stack1.append(x)
        self.stack2 = []
        for i in range(len(self.stack1),0,-1):
            item = self.stack1[i-1]
            self.stack2.append(item)
        self.length+=1
        return self.stack2

    def pop(self):
        removed_item = self.stack2.pop()
        self.stack1 = []
        for i in range(len(self.stack2),0,-1):
            item = self.stack2[i-1]
            self.stack1.append(item)
        self.length-=1
        return removed_item

    def peek(self):
        return self.stack2[self.length-1]

    def empty(self):
        return self.length <1

obj = MyQueue()
obj.push(1)
obj.push(2)
print(obj.peek())
print(obj.pop())
print(obj.empty())
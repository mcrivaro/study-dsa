class MyArr:
    def __init__(self):
        self.length = 0
        self.data = {}

    def get(self, index):
        return self.data[index]

    def push(self, item):
        self.data[self.length] = item
        self.length += 1
        return self.data

    def pop(self):
        last_item = self.data[self.length-1]
        del self.data[self.length-1]
        self.length -= 1
        return last_item

    def delete_at_index(self, index):
        item = self.data[index]
        self.shift_items(index)
        return item

    def shift_items(self, index):
        for item_index in range(index, self.length-1):
            self.data[item_index] = self.data[item_index+1]
        print(self.data[self.length-1])
        del self.data[self.length-1]
        self.length -= 1

    def __repr__(self):
        return f'MyArray length: {self.length}, data: {str(self.data)}'

    def __str__(self):
        return f'MyArray length: {self.length}, data: {str(self.data)}'


if __name__ == "__main__":
    arr = MyArr()
    arr.push('hi')
    arr.push('you')
    arr.push('!')
    arr.pop()
    arr.delete_at_index(0)
    arr.push('are')
    arr.push('nice')
    arr.shift_items(0)
    print(arr)

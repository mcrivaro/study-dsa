class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.__dict__)


class BinarySearchTree():
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return
        current_node = self.root
        children = [current_node.left, current_node.right]
        while any(children):
            if new_node.value < current_node.value and current_node.left:
                current_node = current_node.left
            elif new_node.value > current_node.value and current_node.right:
                current_node = current_node.right
            else:
                break
        if new_node.value < current_node.value:
            current_node.left = new_node
        else:
            current_node.right = new_node

    def insert2(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            while True:
                if new_node.value < current_node.value:
                    if current_node.left is None:
                        current_node.left = new_node
                        return
                    else:
                        current_node = current_node.left
                else:
                    if current_node.right is None:
                        current_node.right = new_node
                        return
                    else:
                        current_node = current_node.right

    def lookup(self, value):
        found = False
        current_node = self.root
        if current_node is None:
            return False
        while not found:
            children = [current_node.left, current_node.right]
            if current_node.value > value and current_node.left:
                current_node = current_node.left
            elif current_node.value < value and current_node.right:
                current_node = current_node.right
            elif current_node.value == value:
                return True
            if not any(children):
                break
        return False

    def lookup2(self, value):
        current_node = self.root
        if current_node is None:
            return False
        while True:
            if value < current_node.value:
                if current_node.left:
                    current_node = current_node.left
                else:
                    return False
            elif value > current_node.value:
                if current_node.right:
                    current_node = current_node.right
                else:
                    return False
            elif value == current_node.value:
                return True

    def lookup3(self, value):
        current_node = self.root
        if current_node is None:
            return False
        while current_node is not None:
            if value < current_node.value:
                current_node = current_node.left
            elif value > current_node.value:
                current_node = current_node.right
            elif value == current_node.value:
                return True
        return False

    def remove(self, value):
        pass

    def __repr__(self):
        return str(self.__dict__)


if __name__ == "__main__":
    my_tree = BinarySearchTree()
    my_tree.insert(9)
    my_tree.insert(4)
    my_tree.insert(20)
    my_tree.insert(1)
    my_tree.insert(6)
    my_tree.insert(15)
    my_tree.insert(170)
    print(my_tree.lookup(10))
    print(my_tree)
    # my_tree.remove(6)

    my_tree2 = BinarySearchTree()
    my_tree2.insert2(9)
    my_tree2.insert2(4)
    my_tree2.insert2(20)
    my_tree2.insert2(1)
    my_tree2.insert2(6)
    my_tree2.insert2(15)
    my_tree2.insert2(170)
    print(my_tree2.lookup2(10))
    print(my_tree2)

    my_tree3 = BinarySearchTree()
    my_tree3.insert(9)
    my_tree3.insert(4)
    my_tree3.insert(20)
    my_tree3.insert(1)
    my_tree3.insert(6)
    my_tree3.insert(15)
    my_tree3.insert(170)
    print(my_tree3.lookup3(170))
    print(my_tree3)
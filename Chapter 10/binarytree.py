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
        # Is node a leaf? -> Delete directly
        # Does it have one child -> Bypass
        # Does it have two childs -> Replace by inorder successor
        current_node = self.root
        parent_node = None
        while current_node:
            if value < current_node.value:
                parent_node = current_node
                current_node = current_node.left
            elif value > current_node.value:
                parent_node = current_node
                current_node = current_node.right
            elif value == current_node.value:
                #option 1: node is a leaf, zero children -> directly
                if (not current_node.left) and (not current_node.right):
                    if parent_node == None:
                        self.root = None
                        return True
                    if current_node.value <= parent_node.value:
                        parent_node.left = None
                    else:
                        parent_node.right = None
                    return True
                #option 2: node has exactly one child -> bypass
                if (current_node.left and not current_node.right) or (
                        current_node.right and not current_node.left):
                    if parent_node == None:
                        if self.root.left:
                            self.root = self.root.left
                        else:
                            self.root = self.root.right
                    if current_node.value < parent_node.value:
                        if current_node.left:
                            parent_node.left = current_node.left
                        else:
                            parent_node.left = current_node.right
                    else:
                        if current_node.left:
                            parent_node.right = current_node.left
                        else:
                            parent_node.right = current_node.right
                    return True
                #option 3: node has two children -> replace node with inorder successor
                # 1. find in order successor
                # 2. copy value too current_node (set inorder successor as child of the parent_node)
                # 3. replace the node by the inorder successor like this:
                #       - remove inorder successor from it's former position (if it has right child, bypass)
                #       - save its parent and the child and do the bypassing normally. parent.left = inorder_successor.right
                #       - set children on the now replaced node
                #       - but only set inorder_successor.right = current_node.right if inorder_successor != current_node.right (resulting in a reference loop)
                if current_node.left and current_node.right:
                    inorder_successor = current_node.right
                    parent_inorder_successor = None
                    right_child_inorder_successor = None
                    # if left child of right child is null -> right child is automatically the inorder successor since while loop won't be executed
                    while inorder_successor.left:
                        parent_inorder_successor = inorder_successor
                        inorder_successor = inorder_successor.left
                        if inorder_successor.left is None:
                            right_child_inorder_successor = inorder_successor.right
                    if parent_node is None:
                        self.root = inorder_successor
                        parent_inorder_successor.left = right_child_inorder_successor
                        self.root.left = current_node.left
                        self.root.right = current_node.right
                        return True
                    else:
                        if inorder_successor.value < parent_node.value:
                            parent_node.left = inorder_successor
                        else:
                            parent_node.right = inorder_successor
                        parent_inorder_successor.left = right_child_inorder_successor
                        if current_node.right != inorder_successor:
                            inorder_successor.right = current_node.right
                        inorder_successor.left = current_node.left
                    return True

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
    my_tree.remove(20)
    # print(my_tree.lookup(10))
    print(my_tree)

    # my_tree2 = BinarySearchTree()
    # my_tree2.insert2(9)
    # my_tree2.insert2(4)
    # my_tree2.insert2(20)
    # my_tree2.insert2(1)
    # my_tree2.insert2(6)
    # my_tree2.insert2(15)
    # my_tree2.insert2(170)
    # print(my_tree2.lookup2(10))
    # print(my_tree2)

    # my_tree3 = BinarySearchTree()
    # my_tree3.insert(9)
    # my_tree3.insert(4)
    # my_tree3.insert(20)
    # my_tree3.insert(1)
    # my_tree3.insert(6)
    # my_tree3.insert(15)
    # my_tree3.insert(170)
    # print(my_tree3.lookup3(170))
    # print(my_tree3)
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self, root):
        self.head = root

    def insert(self, node):
        parent = self.head
        rp = None
        while parent is not None:
            rp = parent
            if node.data < parent.data:
                parent = parent.left
            elif node.data >= parent.data:
                parent = parent.right

        if node.data < rp.data:
            rp.left = node
        elif node.data >= rp.data:
            rp.right = node


def printBST(root):
    if root:
        printBST(root.left)
        print(root.data)
        printBST(root.right)


def minValueNode(node):
    current = node

    # loop down to find the leftmost leaf
    while current.left is not None:
        current = current.left

    return current


def delete_node(root, key):
    if root is None:
        return root

    if key < root.data:
        root.left = delete_node(root.left, key)
    elif key > root.data:
        root.right = delete_node(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp_min = minValueNode(root.right)
        root.data = temp_min.data

        root.right = delete_node(root.right, temp_min.data)

    return root


def main():
    n1 = Node(1)
    n2 = Node(5)
    n3 = Node(10)
    n4 = Node(3)
    n5 = Node(6)
    n6 = Node(7)
    n7 = Node(2)
    n8 = Node(4)
    n9 = Node(8)
    n10 = Node(9)

    b = BST(n1)
    b.insert(n2)
    b.insert(n3)
    b.insert(n4)
    b.insert(n5)
    b.insert(n6)
    b.insert(n7)
    b.insert(n8)
    b.insert(n9)
    b.insert(n10)

    printBST(n1)

    delete_node(n1, 5)
    print("after deletion")
    printBST(n1)


if __name__ == "__main__":
    main()

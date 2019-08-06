class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 0


class Avl:

    def delete(self, root, key):

        # Step 1 - Perform standard BST delete
        if not root:
            return root

        elif key < root.data:
            root.left = self.delete(root.left, key)

        elif key > root.data:
            root.right = self.delete(root.right, key)

        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.getMinValueNode(root.right)
            root.data = temp.data
            root.right = self.delete(root.right,
                                     temp.data)

            # If the tree has only one node,
        # simply return it
        if root is None:
            return root

            # Step 2 - Update the height of the
        # ancestor node
        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))

        # Step 3 - Get the balance factor
        balance = self.get_balance(root)

        # Step 4 - If the node is unbalanced,
        # then try out the 4 cases
        # Case 1 - Left Left
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.rightRotate(root)

            # Case 2 - Right Right
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.leftRotate(root)

            # Case 3 - Left Right
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

            # Case 4 - Right Left
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def insert(self, root, data):
        if root is None:
            root = Node(data)
            return root

        root.height = root.height + 1
        if data < root.data:
            root.left = self.insert(root.left, data)

        else:
            root.right = self.insert(root.right, data)

        # Step 2 - Update the height of the
        # ancestor node
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Step 3 - Get the balance factor
        balance = self.get_balance(root)
        # Step 4 - If the node is unbalanced,
        # then try out the 4 cases
        # Case 1 - Left Left
        if balance > 1 and data < root.left.data:
            return self.rightRotate(root)

            # Case 2 - Right Right
        if balance < -1 and data > root.right.data:
            return self.leftRotate(root)

            # Case 3 - Left Right
        if balance > 1 and data > root.left.data:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

            # Case 4 - Right Left
        if balance < -1 and data < root.right.data:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root


    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)


    def get_height(self, root):
        if root:
            return root.height
        return 0


    def leftRotate(self, z):
        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self.get_height(z.left),
                           self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left),
                           self.get_height(y.right))

        # Return the new root
        return y


    def rightRotate(self, z):
        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + max(self.get_height(z.left),
                           self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left),
                           self.get_height(y.right))

        # Return the new root
        return y

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root

        return self.getMinValueNode(root.left)

def printBST(root):
    if root:
        printBST(root.left)
        print(root.data)
        printBST(root.right)


if __name__ == "__main__":
    avl = Avl()
    root = avl.insert(None, 5)
    root = avl.insert(root, 20)
    root = avl.insert(root, 10)
    root = avl.insert(root, 40)
    root = avl.insert(root, 30)
    root = avl.insert(root, 2)
   # printBST(root)

    avl.delete(root, 30)

    printBST(root)

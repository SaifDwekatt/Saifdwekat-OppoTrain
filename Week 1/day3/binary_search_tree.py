class Node:
    def __init__(self, value):
        self.value = value
        self.left = self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        def _insert(root, value):
            if not root:
                return Node(value)
            if value < root.value:
                root.left = _insert(root.left, value)
            else:
                root.right = _insert(root.right, value)
            return root
        self.root = _insert(self.root, value)

    def search(self, value):
        def _search(node, value):
            if not node:
                return False
            if node.value == value:
                return True
            elif value < node.value:
                return _search(node.left, value)
            else:
                return _search(node.right, value)
        return _search(self.root, value)

    def inorder(self):
        def _inorder(node):
            return _inorder(node.left) + [node.value] + _inorder(node.right) if node else []
        return _inorder(self.root)

if __name__ == "__main__":
    bst = BinarySearchTree()
    for num in [5, 3, 7, 2, 4, 6, 8]:
        bst.insert(num)

    print("Inorder traversal (BST):", bst.inorder())
    print("Search 4:", bst.search(4))
    print("Search 10:", bst.search(10))

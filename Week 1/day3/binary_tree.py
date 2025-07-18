class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_value):
        self.root = Node(root_value)

    def inorder(self, node, result):
        if node:
            self.inorder(node.left, result)
            result.append(node.value)
            self.inorder(node.right, result)

    def preorder(self, node, result):
        if node:
            result.append(node.value)
            self.preorder(node.left, result)
            self.preorder(node.right, result)

    def postorder(self, node, result):
        if node:
            self.postorder(node.left, result)
            self.postorder(node.right, result)
            result.append(node.value)

if __name__ == "__main__":
    bt = BinaryTree(1)
    bt.root.left = Node(2)
    bt.root.right = Node(3)
    bt.root.left.left = Node(4)
    bt.root.left.right = Node(5)

    inorder_result = []
    bt.inorder(bt.root, inorder_result)
    print("Inorder:", inorder_result)

    preorder_result = []
    bt.preorder(bt.root, preorder_result)
    print("Preorder:", preorder_result)

    postorder_result = []
    bt.postorder(bt.root, postorder_result)
    print("Postorder:", postorder_result)

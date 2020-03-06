#Given a Binary tree, convert it into its mirror.

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def mirrorTree(root):

    if root is None:
        return None

    mirrorTree(root.left)
    
    mirrorTree(root.right)

    root.left, root.right = root.right, root.left

    return root

def PrintInOrder(root):
    if root is None:
        return None
    PrintInOrder(root.left)
    print(root.data,end=' ')
    PrintInOrder(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(6)
mirrorTree(root)
print(PrintInOrder(root))

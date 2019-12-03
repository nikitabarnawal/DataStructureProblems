#Given a Binary Tree, convert it into its mirror.

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def mirrorTree(root):
    s = []
    temp = root
    s.append(root)
    while(s):
        q = []
        temp = None
        for node in s:
            node.left,node.right = node.right,node.left
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        s = q
    return root

def PrintInOrder(root):
    if root is None:
        return None
    PrintInOrder(root.left)
    print(root.data,end = ' ')
    PrintInOrder(root.right)


root = Node(1)
root.left = Node(3)
root.right = Node(2)
root.right.left = Node(5)
root.right.right = Node(4)
mirrorTree(root)
print(PrintInOrder(root))

#height of a binary tree

class Node:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def maxDepth(node):
    #import pdb
    #pdb.set_trace()
    if node is None:
        return 0
    else:
        lDepth = maxDepth(node.left)
        rDepth = maxDepth(node.right)

        if (lDepth > rDepth):
            return lDepth+1
        else:
            return rDepth+1

def height(root):
    if root is None:
        return 0
    leftHeight = height(root.left)
    rightHeight = height(root.right)            
    return (max(leftHeight,rightHeight) + 1 ) 


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


print(height(root))

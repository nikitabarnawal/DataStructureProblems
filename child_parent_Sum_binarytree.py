#children parent sum
#Given a binary tree, complete the function that returns true if the tree satisfies the following property:
#For every node, data value must be equal to the sum of data values in left and right children. Consider data value as 0 for NULL child.
#Also, leaves are considered to follow the property.

class Node:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def childParentSum(root):
    if not root:
        return None
    s=[]
    s.append(root)
    while(s):
        q= []
        for node in s:
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            
            if node.left and node.right:
                if node.data != node.left.data + node.right.data:
                    return 0
            if not node.left and node.right:
                if node.data != node.right.data:
                    return 0
            if not node.right and node.left:
                if node.data != node.left.data:
                    return 0
            
        s = q

    return 1

root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.left = Node(5)
root.left.right = Node(3)
root.right.left = Node(2)

print(childParentSum(root))
            

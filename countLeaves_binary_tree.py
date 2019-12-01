#count leaves in a binary tree

class Node:
    
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def countLeaves(node):
    if not node:
        return None
    
    i = 0
    s=[]
    s.append(node)

    while(s):
        q= []
        for node in s:
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            if not node.left and not node.right:
                i+= 1

        s = q
    return i


        
root = Node(1)
root.left = Node(10)
root.right = Node(14)
root.left.left = Node(5)
print(countLeaves(root))
        

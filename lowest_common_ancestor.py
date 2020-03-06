#lowest common ancestor of a binary tree
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None



def lca(root,n1,n2):
    #import pdb
    #pdb.set_trace()
    if not root:
        return None
    if root.data == n1 or root.data == n2:
        return root

    left = lca(root.left,n1,n2)
    right = lca(root.right,n1,n2)


    if left and right:
        return root

    if left != None:
        return left.data
    else:
        return right.data



root = Node(5)
root.left = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
n1 = 3
n2 = 4
print(lca(root,n1,n2))
    

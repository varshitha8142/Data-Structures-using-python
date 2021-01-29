""" Python Script to create a binary search tree and perform search operation """

# Write your code from here
class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.value = key
#function to insert new node with the given key
def insert(root,key):
    if root == None:
        return Node(key)
    elif key>= root.value:
        root.right = insert(root.right,key)
    else:
        root.left = insert(root.left,key)
    return root
#fun to perform inorder tree traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.value)
        inorder(root.right)
#fun for pre order tree traversal
def preorder(root):
    if root:
        print(root.value)
        preorder(root.left)
        preorder(root.right)
#fun to perform postorder tree traversal
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value)
r = Node(5)
r = insert(r,3)
r = insert(r,2)
r = insert(r,4)
r = insert(r,7)
r = insert(r,6)
r = insert(r,8)
print('inorder of binary search tree')
inorder(r)
print('preorder of bst')
preorder(r)
print('postorder of bst')
postorder(r)
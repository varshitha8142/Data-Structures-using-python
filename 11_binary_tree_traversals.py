""" Python Script to create a binary tree and perform various traversals """

# Write your code from here
#CREATRE A ROOT
'''class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


    def printTree(self,data):
        print(self.data)
root=node(10)
root.printTree(2)'''

#INSERTING INTO A TREE
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
def search(root,key):
    if key == None:
        return None
    elif root.value == key:
        return True
    #if given key is greater than rootkey
    if key>root.value:
        return search(root.right,key)
    else:
        return search(root.left,key)
r = Node(5)
r = insert(r,3)
r = insert(r,2)
r = insert(r,4)
r = insert(r,7)
r = insert(r,6)
r = insert(r,8)
k = int(input('eneter a search key:'))
r = search(r,k)
if r == None:
    print('element is not found')
else:
    print('element is found')
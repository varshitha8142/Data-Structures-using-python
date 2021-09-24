""" Python script to create a singly linked list for the following operations
   - Insert a Node at Beginning, at Ending and at a given Position
   - Delete a Node at Beginning, at Ending and at a given Position
   - Search, Count the Number of Nodes and Display """

# Write your code from here(1)
class node:
   def __init__(self,data):
      self.data=data
      self.next=None
head=0
for i in range(4):
   if(head==0):
      head=node(i)
      n=head
   else:
      n.next=node(i)
      n=n.next

#insert a Node at Beginning
def f(t):
    global head
    n=head
    newnode=node(int(input("enter a number to insert at first")))
    t=n
    
    newnode.next=n
    head=newnode
f(head)

#insert a node at given position
def fa(p):
    c=int(input("enter a number to insert at given position"))
    newnode=node(c)
    
    pos=3
    c=1
    while(c<pos):
        p=p.next
        c+=1
    newnode.next=p.next
    p.next=newnode
fa(head)
    
#insert a node at end
'''def end(t):
    newnode=node(8)
    while(t.next!=None):
        t=t.next
    t.next=newnode
    newnode.next=None
    print(newnode.data)
end(head)'''
def fp(b):
    b=int(input("enter a number to insert at end"))
    newnode=node(b)
    b=n
    b.next=newnode
    newnode.next=None
fp(head)

n=head
while(n!=None):
    print(n.data)
    n=n.next   
# Write your code from here(2)
#del the node at begining



#DEL A NODE AT BEGINNING
def del_at_begin(self):
    global head
    t=n
    head=head.next
    del t

del_at_begin(head)  
n=head

#DEL AT GIVEN POSITION IN SLL
def delete(t):
    c=1
    p=int(input("enter the position :"))
    while(c<p):
        n=t
        t=t.next
        c+=1
    n.next=t.next
    del t
delete(head)
print("after deletion at begin,pos,end:")
while(n!=None):
    print(n.data)
    n=n.next

#DELETE A NODE AT END


#Search(linear search)
class node:
   def __init__(self,data):
      self.data=data
      self.next=None
head=0
key=int(input("enter key value"))
b=0
n=int(input("enter no.of nodes:"))
for i in range(n):
    c=int(input("enter the data:"))
    if(head==0):
        head=node(c)
        n=head
    else:
        n.next=node(c)
        n=n.next
    t=n
    if(key==t.data):
        b+=1
    t=t.next
if(b==1):
    print("element node is found")
            
else:
    print("element node is not found")

#count no.of nodes
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=0
count=0
n=int(input("enter no.of nodes to count the values:"))
for i in range(n):
    c=int(input("enter data:"))

    if(head==0):
        head=Node(c)
        n=head
    else:
        n.next=Node(c)
        n=n.next
    count+=1
print("The total number of nodes is:",count)







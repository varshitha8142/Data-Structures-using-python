""" Python script to create a doubly linked list for the following operations
   - Insert a Node at Beginning, at Ending and at a given Position
   - Delete a Node at Beginning, at Ending and at a given Position
   - Search, Count the Number of Nodes and Display """

# Write your code from here
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
head=0
a=int(input("enter no.of nodes:"))
for i in range(a):
    b=int(input())
    if(head==0):
        head=node(b)
        n=head
    else:
        t=n
        n.next=node(b)
        n=n.next
        t.next=n
        n.prev=t
        
#insert at begin
def begin(p):
    newnode=node(int(input(" enter data at begin")))
    n.prev=newnode
    newnode.next=p
    global head
    head=newnode
begin(head)

#insert node at pos
def pos(p):
    newnode=node(int(input(" enter data at position")))
    c=1
    pos=3
    while(c<pos):
        p=p.next
        c+=1
    
    newnode.prev=p
    newnode.next=p.next
    p.next=newnode
    p=newnode.next
    p.prev=newnode
pos(head)
    
#insert node at end
def end(p):
    newnode=node(int(input(" enter data at end")))
    newnode.prev=n
    n.next=newnode
end(head)

n=head
print("after insertion:")
while(n!=None):
   print(n.data)
   n=n.next

#deletion
    
#del node at begining
def begin_del(p):
    global head
    t=head
    head=head.next
    head.prev=None
    del t
begin_del(head)


#del node at position
def del_pos(t):
    pos=3
    c=1
    while(c<pos):
        n=t
        t=t.next
        c+=1
        n.next=t.next
        t.prev=n
del_pos(head)


#del node at end
def end_del(p):
    t=p
    while(p.next!=None):
        t=p
        p=p.next
    t.next=None
end_del(head)

n=head
print("after deletion at begin,end,pos")
while(n!=None):
   print(n.data)
   n=n.next


#SEarch

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
head=0
key=int(input("enter key"))
c=0
n=int(input("no.of nodes:"))
for i in range(n):
    c=int(input())
    
    if(head==0):
        head=Node(c)
        n=head
    else:
        t=n
        n.next=Node(c)
        n=n.next
        t.next=n
        n.prev=t
    t=n
    if(key==t.data):
        c+=1
if(c==1):
    print("key is found")
else:
    print("not found")

#count
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
head=0
count=0
n=int(input("enter no.of nodes to count the values:"))
for i in range(n):
    c=int(input("enter data:"))

    if(head==0):
        n=head=Node(c)
    else:
        t=n
        n.next=Node(c)
        n=n.next
        n.prev=t
    count+=1
print("The total number of nodes is:",count)
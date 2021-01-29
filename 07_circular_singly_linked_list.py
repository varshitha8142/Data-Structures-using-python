""" Python Script to create a Circular singly linked list for adding and 
deleting a Node. """

# Write your code from here
#add an element before & after key
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=0
key=2
c=0
b=[]
n=int(input("enter numb of nodes:"))
for i in range(n):
    c=(int(input()))
    d=b.append(c)
    if(head==0):
        head=node(c)
        n=head
    else:
        n.next=node(c)
        n=n.next
n.next=head
key=int(input("enter key value to insert after key:"))
newnode=node(int(input("enter newnode:")))
k=0
if(key in b):
    while(n):
        if n.data==key:
            newnode.next=n.next
            n.next=newnode
            k+=1
            break
        else:
            n=n.next
    n=head
    p=n
    print(p.data)
    p=p.next
    while(p!=n):
        print(p.data)
        p=p.next

    key=int(input("enter key value to insert before key:"))
    newnode=node(int(input("enter newnode:")))
    

    while(n):
        if n.data==key:
            newnode.next=n
            t.next=newnode
            k+=1
            break
        else:
            t=n
            n=n.next
else:
    print("key not found")

n=head
p=n
print(p.data)
p=p.next
while(p!=n):
    print(p.data)
    p=p.next

#del an element before & after key
def fb(n):
    k=0
    key=int(input("enter key to del after element"))
    while(n):
        if n.data==key:
            
            t=n.next
            b=t.next
            t.next=None
            n.next=b
            k+=1
            break
        else:
            
            t=n
            n=n.next      
fb(head)
n=head
d=n
print(d.data)
d=d.next
while(d!=n):
    print(d.data)
    d=d.next
#this is
def fp(p):
    n=head
    k=0
    key=int(input("enter key to del before key"))
    while(n):
        if (n.data==key):
            if(p.next==t):
                t.next=None
                del t
                p.next=n
                k+=1
                break
            p=p.next
        else:
            t=n
            n=n.next
        
fp(head)
n=head
p=n
print(p.data)
p=p.next
while(p!=n):
    print(p.data)
    p=p.next
 #del at key

def f(n):
    k=0
    key=int(input("del particular key element:"))
    while(n):
        if n.data==key:
            n=n.next
            t.next=n
            del t
            k+=1
            break
        else:
            
            t=n
            n=n.next
        
f(head)
n=head
p=n
print(p.data)
p=p.next
while(p!=n):
    print(p.data)
    p=p.next
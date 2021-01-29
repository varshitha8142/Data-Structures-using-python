""" Python Script to create a stack and perform various operations on it """

# Write your code from here
class Stack:
    def __init__(self):
        self.stack=[]
        self.top=-1
    def push(self):
        #self.stack=[]
        #self.top=-1
        a=int(input("no.of values"))
        for i in range((a)):
            c=int(input())
            self.top+=1
            b=self.stack.append(c)
    def is_empty(self):
        if(self.stack==0):
            return True
        else:
            return False
    def pop(self):
        if(self.is_empty()):
            print("stack under flow")
        else:
            print("Del element is",self.stack.pop())
            self.top-=1
    def display(self):
        if(self.is_empty()):
            print("empty")
        else:
            print("after del these are remaining values:")
            for i in range(self.top,-1,-1):
                print(self.stack[i])


s=Stack()
Stack.push(s)
s.is_empty()
s.pop()
s.display()


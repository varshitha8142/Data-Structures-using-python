""" Python Script to create a queue and perform various operations on it """

# Write your code from here

class Queue:
    def __init__(self):
        self.queue=[]
        self.rear=0
        self.front=0
    def enqueue(self):
        a=int(input("enter no.of values:"))
        for i in range(a):
            b=int(input())
            c=self.queue.append(b)
            self.rear+=1
    def is_empty(self):
        if (len(self.queue)==0):
            return True
        else:
            return False
    def dequeue(self):
        if(self.is_empty()):
            print("underflow")
        else:
            print("del element is:",self.queue.pop(0))
    def display(self):
        if(self.is_empty()):
            print(" ")
        else:
            print("The elements in the queue are:")
            for i in range(len(self.queue)):
                print(self.queue[i])
    def length(self):
        print ("len of queue is:",len(self.queue))
        
    def peek(self):
        if self.is_empty():
            print("underflow")
        else:
            print("Top most element in queue :",self.queue[0])
q=Queue()
Queue.enqueue(q)
q.dequeue()
q.display()
q.length()
q.peek()
q.display()

        
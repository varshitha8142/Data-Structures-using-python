""" Python Script to read a linear list of items and store it in an array.
   - Copy the contents from one array to another array
   - Copy the contents from one array to another array in reverse order
   - Delete the duplicate elements from an array. """

# Write your code from here
#(1)
from array import*
a=int(input("enter no.of values:"))
l=array('i',[])
for i in range(a):
   l.append(int(input()))
b=(l)
print(b)

#(2)
b=int(input("enter no.of values:"))
l=array('i',[])
for i in range(b):
   l.append(int(input()))
#b=(l[::-1])
l.reverse()
print(l)

#(3)
c=int(input("enter no.of values:"))
l=array('i',[])
for i in range(c):
   l.append(int(input()))
b=set(l)
print(list(b))

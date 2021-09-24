""" Python script to perform linear search in an array. """

# Write your code from here
from array import*
key=int(input("enter key value:"))
c=0
n=int(input("enter values:"))
array=array('i',[])
for i in range(n):
    array.append(int(input()))
while(key in array):  
    print("element is  found")
    break

if(key not in array):
    print("element not found")
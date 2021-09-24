""" Python Script to find sum of digits of a number """

# Write your code from here
a=int(input("enter a number"))
sum=0
while(a>0):
    sum=sum+a%10
    a=a//10
print(sum)



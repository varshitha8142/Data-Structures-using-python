""" Python Script to check whether a given number is perfect  """

# Write your code from here
num=int(input("enter number"))
sum=0
for i in range(1,num):
    if (num%i==0):
        sum=sum+i
if(num==sum):
    print('perfect')
else:
    print('not perfect')
        
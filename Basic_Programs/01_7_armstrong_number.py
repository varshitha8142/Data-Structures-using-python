""" Python Script to find whether a number is armstrong or not """

# Write your code from here
a=int(input("enter number :"))
sum=0
num=a
n=len(str(a))
while a > 0:
   digit = a % 10
   sum =sum+digit ** n
   a //= 10
if(num==sum):
    print('it is armstrong ')
else:
    print('no it is not armstrong numb')

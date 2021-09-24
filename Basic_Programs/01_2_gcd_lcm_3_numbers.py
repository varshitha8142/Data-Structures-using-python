""" Python Script to find GCD and LCM of 2 numbers """

# Write your code from here
num1 = int(input("enter 1st value"))
num2 = int(input("enter 2 nd value"))
num3 = int(input("enter 3 rd value"))
if(num1 > num2 ):   # Use If condition to find the greatest number among these two.
    max= num1
elif(num1<num2):
    max= num2
else:
    max=num3
while(True):
    if(max % num1 == 0 and max % num2 == 0 and max%num3==0) :   
        print(max)
        break
    max= max+ 1
# code for gcd
from math import gcd
print(f"gcd of num1 ,num2 is {gcd(gcd(num1,num2),num3)}")


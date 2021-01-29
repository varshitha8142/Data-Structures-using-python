""" Python Script to find GCD and LCM of 3 numbers """

# Write your code from here
num1 = int(input("enter 1st value"))
num2 = int(input("enter 2 nd value"))
if(num1 > num2 ):   # Use If condition to find the greatest number among these two.
    max= num1
else:
    max= num2
while(True):
    if(max % num1 == 0 and max % num2 == 0):   
        print(max)
        break
    max= max+ 1
# code for gcd
import math
print("gcd of num1 ,num2",math.gcd(num1,num2))

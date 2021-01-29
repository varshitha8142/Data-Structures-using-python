""" Python Script to find twin primes upto a specified limit """

# Write your code from here
def is_prime(num):
    for i in range(2, num):

        if num % i == 0:

            return False

    return True

def generate_twins(start, end):

    for i in range(start, end):

        j = i + 2

        if(is_prime(i) and is_prime (j)):

            print((1,3))

x=int(input("enter any first limit"))

y=int(input("enter the last limit"))

generate_twins (x,y)

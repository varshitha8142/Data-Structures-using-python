""" Python script to perform binary search on a list stored in an array """

# Write your code from here
ls=[]
ls.append(int(input("1st numb")))
ls.append(int(input("2 numb")))
ls.append(int(input("3rd numb")))
ls.append(int(input("4th numb")))
lst=sorted(ls)
key=int(input("enter  a key :"))
l=0
flag=0
u=len(lst)-1
while l<=u:
    mid=(l+u)//2
    if lst[mid]==key:
        flag=1
        break
    else:
        if (lst[mid]<key):
            l=mid+1
        else:
            u=mid-1
if (flag==1):
    print('element is found')
else:
    print('element is not found')
#Inseration Sort:
def inserationsort(arr):
    n=len(arr)
    l=[]
    for i in range(1,n-1):
        currentvalue=arr[i]
        position=i
        while position>0 and arr[position-1]>currentvalue:
            arr[position]=arr[position-1]
            position=position-1
            arr[position]=currentvalue
    for i in range(n):
        l.append(arr[i])
    print("the sorting after insertion",l)
arr=[2,4,1,0,5,8]
inserationsort(arr)

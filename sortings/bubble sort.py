#bubble sort
def bubblesort(arr):
    l=[]
    n=len(arr)
    temp=0    
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    for i in range(n):
        l.append(arr[i])
    print("the sorting after bubble sort",l)
arr=[64,34,25,12,22,11,90]
bubblesort(arr)

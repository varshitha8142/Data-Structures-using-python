""" Python Script to implement various sorting techniques: 
    - Insertion sort
    - Selection Sort
    - Bubble Sort
    - Merge Sort
    - Quick Sort 
    [Compare with Python's Built-In Sorting Functions also]  """

# Write your code from here
#Selection sort:
def s(a):
    n=len(a)
    l=[]
    for i in range(n):
        min=i
        for j in range(i+1,n):
            if(a[j]<a[min]):
                min=j
        t=a[i]
        a[i]=a[min]
        a[min]=t
    for i in range(n):
        l.append(a[i])
    print("the sorting after selection sort",l)
a=[13,4,9,5,3]
s(a)
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
#merge sort
def merge(a,b):
    c=[]
    a_ind,b_ind=0,0
    while a_ind<len(a) and b_ind<len(b):
        if a[a_ind]<b[b_ind]:
            c.append(a[a_ind])
            a_ind+=1
        else:
            c.append(b[b_ind])
            b_ind+=1 
    if a_ind==len(a):
        c.extend(b[b_ind:])
    else:
        c.extend(a[a_ind:])
    return c
#Quick Sort
def partition(arr,low,high):
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<=pivot:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1
def quick_sort(arr, low, high):
    if len(arr)==1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)
    return arr
arr=[11,16,2,8,1,9,4,7]
quick_sort(arr,0,7)
print("the sorting after quick sort",arr)
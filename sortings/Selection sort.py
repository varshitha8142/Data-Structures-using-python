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

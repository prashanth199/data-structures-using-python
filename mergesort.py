import numpy as np
def merge(arr,beg,mid,end):

    n1 = mid-beg+1
    n2 = end-mid
    la = []
    ra = []

    for i in range(0,n1):
        la.insert(i,arr[beg+i])
        

    for j in range(0,n2):
        ra.insert(i,arr[mid+1+j])
        
    

    i=0
    j=0
    k=beg

    while i<n1 and j<n2:
        if la[i]<=ra[j]:
            arr[k] = la[i]
            i+=1
        else:
            arr[k] = ra[j]
            j+=1
        k+=1
     
    while(i<n1):
        arr[k] = la[i]
        i+=1
        k+=1
    while(j<n2):
        arr[k] = ra[j]
        j+=1
        k+=1


def mergeSort(arr,beg,end):
    if beg<end:
        mid = (beg+end)//2
        mergeSort(arr,beg,mid)
        mergeSort(arr,mid+1,end)
        merge(arr,beg,mid,end)


a = [68, 13, 1, 49, 58]
print("before Sort")
print(a)
mergeSort(a,0,len(a)-1)
print("after sort")
print(a)
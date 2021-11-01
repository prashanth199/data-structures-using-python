

def selectionsort(arr):
    for i in range(0,len(arr)-1):
        indexMin = i 

        for j in range(i+1,len(arr)):
            if arr[j]<arr[indexMin]:
                indexMin = j

        if(indexMin!=i):
            print("items swapped: [{},{}]".format(arr[i],arr[indexMin]))
            
            arr[i] , arr[indexMin] = arr[indexMin],arr[i]
        
        print("iteration #{}".format(i+1))
        print(arr)


n = input("enter list of numbers").split()   
print(n)
selectionsort(n)
print("final Output")
print(n)     
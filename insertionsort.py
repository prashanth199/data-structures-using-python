def insertionSort(arr):
    for i in range(1,len(arr)):
        # value to be inserted
        valueToInsert = arr[i]
        #position where number is inserted
        holePosition = i

        #check if previous number is larger than value to be inserted
        while(holePosition>0 and arr[holePosition-1]>valueToInsert):
            arr[holePosition]=arr[holePosition-1]
            holePosition = holePosition-1
            print("item moved:{}".format(arr[holePosition]))
        if(holePosition!=i):
            arr[holePosition]=valueToInsert
            print("item inserted :{} at position:{}".format(valueToInsert,holePosition))
        print("iteration #{}".format(i))
        print(arr)
    return arr
        

n = input('enter list of numbers').split()
print('before sort')
print(n)
insertionSort(n)
print('after sort')
print(n)

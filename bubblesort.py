
def bubbleSort(list):
    """This function generates a sorted list using bubblesort technique

    Args:
        list (list): list of items
    """
    listlength = len(list)

    for i in range(listlength-1):
        swapped = False

        for j in range(listlength-1-i):
            x = "items compared [{},{}]".format(list[j],list[j+1])
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                swapped = True
                print(x+"=>swapped[{},{}]".format(list[j],list[j+1]))
            else:
                print(x+"=>not swapped")

        if(not swapped):
            break
        
        print("iteration #{}".format(i+1))
        
        print(list)


array = input("Enter Numbers").split()

print(array)
bubbleSort(array)
print("Final Output")
print(array)


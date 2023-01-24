def bubbleSort(inputList):
    # print("hello")
    # print(inputList)
    lengthOftheList = len(inputList)
    # Traverse through all the elements
    for i in range(lengthOftheList):
        # last i elements are already in place
        for j in range(0,lengthOftheList - i - 1):
            # Swap if the element found is greater than the next element
            if inputList[j] > inputList[j + 1] : 
                temp = inputList[j]
                inputList[j] = inputList[j + 1]
                inputList[j+1] = temp
    # print(inputList)
    return inputList


def selectionSort(inputList):
    #identifying the length of the list
    lengthOftheList = len(inputList)
    # traversing through the list
    for i in range(lengthOftheList):
        # assuming the first element as first element in the unsorted array
        min_idx = i
        # traversing through the list from i+1 
        for j in range(i+1, lengthOftheList):
            # comparing the element with the unsorted array element 
            if inputList[min_idx] > inputList[j]:
                min_idx = j
        # swapping the elements 
        inputList[i], inputList[min_idx] = inputList[min_idx], inputList[i]

def inserationSort(inputList):
    # print(inputList)
    lengthOftheList = len(inputList)
    # traversing through the list
    for i in range(1,lengthOftheList):
        element = inputList[i]
        j = i - 1 
        #comparing with each element on the left until a smaller element is found 
        while j>= 0 and inputList[j] > element:
            inputList[j+1] = inputList[j]
            j = j - 1
        # changing the positon and placing the smaller value before the element
        inputList[j + 1 ] = element
    print(inputList)
    return inputList

def mergeSort(list):
    if len(list) > 1:
        #finding the middle element of the list
        mid = len(list) // 2
        #separating left side from the middle to left list
        left_list = list[:mid]
        #separating right from from the middle and assigning to right list 
        right_list = list[mid:]
        # recursive call to mergeSort to sort left list and right list 
        mergeSort(left_list)
        mergeSort(right_list)
        i = j = k = 0
        # loop until we reach length of either right or left list and place them in correct position
        while i < len(left_list) and j < len(right_list):
            if left_list[i] <= right_list[j]:
                list[k] = left_list[i]
                i += 1
            else:
                list[k] = right_list[j]
                j += 1
            k += 1
        # checking if there any left elemets in left list 
        while i < len(left_list):
            list[k] = left_list[i]
            i += 1
            k += 1
        # checking if there is any elements in the right list 
        while j < len(right_list):
            list[k] = right_list[j]
            j += 1
            k += 1
    return list


def heap(arrList, n, i):
    #Initializing the root to be the largest
    largest_element = i  
     # Left node
    left = 2 * i + 1   
    # right node  
    rightNode = 2 * i + 2     
     # Check if the left child of root node exists and is greater than the root
    if left < n and arrList[largest_element] < arrList[left]:
        largest_element = left
    # Compare the right right side of the root
    if rightNode < n and arrList[largest_element] < arrList[rightNode]:
        largest_element = rightNode
    # If needed then change the element
    if largest_element != i:
        # Finally heapify the root
        arrList[i], arrList[largest_element] = arrList[largest_element], arrList[i] 
        # recursive call to at the child node to make it max heap tree 
        heap(arrList, n, largest_element)
# use heapify function to sort the list
def heapSort(arr):
    n = len(arr)

    for i in range(n//2 - 1, -1, -1):
        heap(arr, n, i)
 
    for i in range(n-1, 0, -1):
        # swap 
        arr[i], arr[0] = arr[0], arr[i]  
        heap(arr, i, 0)

def divide(arr, start, end):
    # setting the pivot index as first elemnt
    pivot_index = start 
    # pointer to pivot first index 
    pivot = arr[pivot_index]
    while start < end:
        while start < len(arr) and arr[start] <= pivot:
            start += 1
        while arr[end] > pivot:
            end -= 1
        #checking if low and high have crossed
        if(start < end):
            arr[start], arr[end] = arr[end], arr[start]
    #swapping pivot with end so that pivot is at its right
    arr[end], arr[pivot_index] = arr[pivot_index], arr[end]
    return end

def quickSort(arr, start, end):

    if (start < end):
        # check if elements smaller than pivot is towards the left and greater is towards the right
        p = divide(arr, start, end)
        # recursive call to sort smaller than pivot 
        quickSort(arr, start, p - 1)
        # recursive call to sort greater than pivot 
        quickSort(arr, p + 1, end)

def divThreeWay(arrList, last, start, mid):
    # partition into 3 ways : 1) values greater than pivot , 2) values = pivot and , 3) values < than pivot
    pivot = arrList[last]
    end = last
     # Iterate while mid is not greater than end.
    while (mid[0] <= end):
        # change position if value is less than pivot 
        if (arrList[mid[0]] < pivot): 
            arrList[mid[0]], arrList[start[0]] = arrList[start[0]], arrList[mid[0]] 
            mid[0] = mid[0] + 1
            start[0] = start[0] + 1
        # change position if value > than pivot 
        elif (arrList[mid[0]] > pivot):
            arrList[mid[0]], arrList[end] = arrList[end], arrList[mid[0]]
            end = end - 1
             
        else:
            mid[0] = mid[0] + 1
 
def quickSortThreeWay(arrList, first, last):
     # base condition for 0 or 1 elements
    if (first >= last):
        return
    # Second case when an array contain only 2 elements
    if (last == first + 1):
        if (arrList[first] > arrList[last]): 
            arrList[first], arrList[last] = arrList[last], arrList[first]
            return
    # Third case when an array contain more than 2 elements
    start = [first]
    mid = [first]
    # partition the array
    divThreeWay(arrList, last, start, mid)
    # recussive call to sort sublist lesser than pivot 
    quickSortThreeWay(arrList, first, start[0] - 1)
     # recussive call to sort sublist greater than pivot 
    quickSortThreeWay(arrList, mid[0], last)


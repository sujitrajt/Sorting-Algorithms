import time
import random
import matplotlib.pyplot as plt
from sort import *
import tkinter as tk
import copy
inputList = []
randomArrayList = []

# function to clear the text box
def clearInput():
    text2.delete(1.0, "end-1c")
    text3.delete(1.0, "end-1c")
    # clearing the text so we can re intialise the input list to the original
    # inputList.clear()
    # inputList.extend(list(map(int, (text1.get(1.0, "end-1c")).split(","))))
    # print(inputList)


# function to perform bubble sort on the input list and calculate the time it take to finish soring


def bubble_sort(arr):
    global randomArrayList
    length = int(text1.get(1.0, "end-1c"))
    # print(length)
    clearInput()
    # checking if the randomlist empty of differnt value has been entered by the user
    if randomArrayList == [] or len(randomArrayList) != length:
        minimumSize = int(text1.get(1.0, "end-1c"))
        for i in range(minimumSize+1):
            randomArrayList = random.sample(range(-1000, 1000), i)
    print(randomArrayList)
    # taking a copy already generated randomArray so sorting happens on the same array
    unsortedArray = copy.deepcopy(randomArrayList)
    print("unsorted bubble", unsortedArray)
    start_time = time.perf_counter()
    bubbleSort(unsortedArray)
    tot_time = time.perf_counter() - start_time
    details_str = "SIZE OF ARRAY : " + \
        str(len(unsortedArray))+"\nBUBBLE SORT"+"\nTIME TAKEN : "+str(tot_time)
    text3.insert('end-1c', details_str)
    # displaying the sorted array into the text box
    if (unsortedArray != []):
        text2.insert('end-1c', str(unsortedArray))
    print("bubblesort", unsortedArray)


# function to perform inseration sort on the input list and calculate the time it take to finish soring
def insertSort(arr):
    global randomArrayList
    length = int(text1.get(1.0, "end-1c"))
    clearInput()
    if randomArrayList == [] or len(randomArrayList) != length:
        minimumSize = int(text1.get(1.0, "end-1c"))
        for i in range(minimumSize+1):
            randomArrayList = random.sample(range(-1000, 1000), i)
    unsortedArray = copy.deepcopy(randomArrayList)
    print("unsorted insertsort", unsortedArray)
    start_time = time.perf_counter()
    inserationSort(unsortedArray)
    tot_time = time.perf_counter() - start_time
    details_str = "SIZE OF ARRAY : " + \
        str(len(unsortedArray))+"\nINSERTION SORT" + \
        "\nTIME TAKEN : "+str(tot_time)
    text3.insert('end-1c', details_str)
    if (unsortedArray != []):
        text2.insert('end-1c', str(unsortedArray))
    print("insertsort", unsortedArray)

# function to perform select sort on the input list and calculate the time it take to finish soring


def selectSort(arr):
    global randomArrayList
    length = int(text1.get(1.0, "end-1c"))
    clearInput()
    if randomArrayList == [] or len(randomArrayList) != length:
        minimumSize = int(text1.get(1.0, "end-1c"))
        for i in range(minimumSize+1):
            randomArrayList = random.sample(range(-1000, 1000), i)
    unsortedArray = copy.deepcopy(randomArrayList)
    print("unsorted slectsort", unsortedArray)
    start_time = time.perf_counter()
    selectionSort(unsortedArray)
    tot_time = time.perf_counter() - start_time
    details_str = "SIZE OF ARRAY : " + \
        str(len(unsortedArray))+"\nSELECTION SORT" + \
        "\nTIME TAKEN : "+str(tot_time)
    text3.insert('end-1c', details_str)
    if (unsortedArray != []):
        text2.insert('end-1c', str(unsortedArray))
    print("selectSort", unsortedArray)


# function to perform merge sort on the input list and calculate the time it take to finish soring
def merge_Sort(arr):
    global randomArrayList
    length = int(text1.get(1.0, "end-1c"))
    clearInput()
    if randomArrayList == [] or len(randomArrayList) != length:
        minimumSize = int(text1.get(1.0, "end-1c"))
        for i in range(minimumSize+1):
            randomArrayList = random.sample(range(-1000, 1000), i)
    unsortedArray = copy.deepcopy(randomArrayList)
    print("unsorted merge", unsortedArray)
    start_time = time.perf_counter()
    mergeSort(unsortedArray)
    total_time = time.perf_counter() - start_time
    details_str = "SIZE OF ARRAY : " + \
        str(len(unsortedArray))+"\nMERGE SORT" + \
        "\nTIME TAKEN : "+str(total_time)
    text3.insert('end-1c', details_str)
    if (unsortedArray != []):
        text2.insert('end-1c', str(unsortedArray))
    print("merge_Sort", unsortedArray)


# function to perform heap sort on the input list and calculate the time it take to finish soring
def heap_Sort(arr):
    global randomArrayList
    length = int(text1.get(1.0, "end-1c"))
    clearInput()
    if randomArrayList == [] or len(randomArrayList) != length:
        minimumSize = int(text1.get(1.0, "end-1c"))
        for i in range(minimumSize+1):
            randomArrayList = random.sample(range(-1000, 1000), i)
    unsortedArray = copy.deepcopy(randomArrayList)
    print("unsorted heap", unsortedArray)
    start_time = time.perf_counter()
    heapSort(unsortedArray)
    total_time = time.perf_counter() - start_time
    details_str = "SIZE OF ARRAY : " + \
        str(len(unsortedArray))+"\nHEAP SORT"+"\nTIME TAKEN : "+str(total_time)
    text3.insert('end-1c', details_str)
    if (unsortedArray != []):
        text2.insert('end-1c', str(unsortedArray))
    print("heap_Sort", unsortedArray)


# function to perform quick sort on the input list and calculate the time it take to finish soring
def quick_Sort(inputArray):
    global randomArrayList
    length = int(text1.get(1.0, "end-1c"))
    clearInput()
    if randomArrayList == [] or len(randomArrayList) != length:
        minimumSize = int(text1.get(1.0, "end-1c"))
        for i in range(minimumSize+1):
            randomArrayList = random.sample(range(-1000, 1000), i)
    unsortedArray = copy.deepcopy(randomArrayList)
    print("unsorted quick", unsortedArray)
    lengthofInput = len(unsortedArray)
    start_time = time.perf_counter()
    quickSort(unsortedArray, 0, lengthofInput-1)
    total_time = time.perf_counter() - start_time
    details = "SIZE OF ARRAY : " + \
        str(len(unsortedArray))+"\nquicksort"+"\nTIME TAKEN : "+str(total_time)
    text3.insert('end-1c', details)
    if (unsortedArray != []):
        text2.insert('end-1c', str(unsortedArray))
    print("quick_Sort", unsortedArray)


# function to perform 3 way quick sort on the input list and calculate the time it take to finish soring
def quickSort_3Way(inputList):
    global randomArrayList
    length = int(text1.get(1.0, "end-1c"))
    clearInput()
    if randomArrayList == [] or len(randomArrayList) != length:
        minimumSize = int(text1.get(1.0, "end-1c"))
        for i in range(minimumSize+1):
            randomArrayList = random.sample(range(-1000, 1000), i)
    unsortedArray = copy.deepcopy(randomArrayList)
    print("unsorted 3quick", unsortedArray)
    lengthofInput = len(unsortedArray)
    start_time = time.perf_counter()
    quickSortThreeWay(unsortedArray, 0, lengthofInput-1)
    total_time = time.perf_counter() - start_time
    details = "SIZE OF ARRAY : " + \
        str(len(unsortedArray))+"\n3 way quicksort" + \
        "\nTIME TAKEN : "+str(total_time)
    text3.insert('end-1c', details)
    if (unsortedArray != []):
        text2.insert('end-1c', str(unsortedArray))
    print("quickSort_3Way", unsortedArray)


def runTimeComp():
    minimumSize = int(text4.get(1.0, "end-1c"))
    maximumSize = int(text5.get(1.0, "end-1c"))
    bubblesortTime = []
    inserationSortTime = []
    selectionSortTime = []
    mergeSortTime = []
    quickSortTime = []
    quick3wayTime = []
    heapSortTime = []
    for i in range(minimumSize, maximumSize):
        randomArrayList = random.sample(range(-1000, 1000), i)
        print("Random array", randomArrayList)
        unsortedRandomArray = randomArrayList.copy()
        startTime = time.perf_counter()
        bubbleSort(unsortedRandomArray)
        TotalTime = time.perf_counter() - startTime
        bubblesortTime.append(TotalTime)
        print(bubblesortTime)
        #######################################################
        print("Random array", randomArrayList)
        unsortedRandomArray = randomArrayList.copy()
        startTime = time.perf_counter()
        selectionSort(unsortedRandomArray)
        TotalTime = time.perf_counter() - startTime
        selectionSortTime.append(TotalTime)
        print(selectionSortTime)
        #########################################################
        print("Random array", randomArrayList)
        unsortedRandomArray = randomArrayList.copy()
        startTime = time.perf_counter()
        mergeSort(unsortedRandomArray)
        TotalTime = time.perf_counter() - startTime
        mergeSortTime.append(TotalTime)
        print(mergeSortTime)
        #########################################################
        print("Random array", randomArrayList)
        unsortedRandomArray = randomArrayList.copy()
        startTime = time.perf_counter()
        inserationSort(unsortedRandomArray)
        TotalTime = time.perf_counter() - startTime
        inserationSortTime.append(TotalTime)
        print(inserationSortTime)
        #########################################################
        print("Random array", randomArrayList)
        unsortedRandomArray = randomArrayList.copy()
        startTime = time.perf_counter()
        heapSort(unsortedRandomArray)
        TotalTime = time.perf_counter() - startTime
        heapSortTime.append(TotalTime)
        print(heapSortTime)
        #########################################################
        print("Random array", randomArrayList)
        unsortedRandomArray = randomArrayList.copy()
        lengthOfUnsortedArray = len(unsortedRandomArray)
        startTime = time.perf_counter()
        quickSort(unsortedRandomArray, 0, lengthOfUnsortedArray-1)
        TotalTime = time.perf_counter() - startTime
        quickSortTime.append(TotalTime)
        print(heapSortTime)
        #########################################################
        print("Random array", randomArrayList)
        unsortedRandomArray = randomArrayList.copy()
        lengthOfUnsortedArray = len(unsortedRandomArray)
        startTime = time.perf_counter()
        quickSortThreeWay(unsortedRandomArray, 0, lengthOfUnsortedArray-1)
        TotalTime = time.perf_counter() - startTime
        quick3wayTime.append(TotalTime)
        print(heapSortTime)
    text6.insert('end-1c', randomArrayList)

    plt.plot(list(range(minimumSize, maximumSize)), bubblesortTime,
             color="red", label="Bubble sort Run Time")
    plt.plot(list(range(minimumSize, maximumSize)), selectionSortTime,
             color="blue", label="Selection sort Run Time")
    plt.plot(list(range(minimumSize, maximumSize)), mergeSortTime,
             color="green", label="Mergesort Run Time")
    plt.plot(list(range(minimumSize, maximumSize)), inserationSortTime,
             color="yellow", label="Inseration Run Time")
    plt.plot(list(range(minimumSize, maximumSize)), heapSortTime,
             color="black", label="HeapSort Run Time")
    plt.plot(list(range(minimumSize, maximumSize)), quickSortTime,
             color="purple", label="Quick Sort Run Time")
    plt.plot(list(range(minimumSize, maximumSize)), quick3wayTime,
             color="orange", label="3 way Quick Sort Run Time")

    plt.legend()
    plt.show()
    # print(maximumSize,minimumSize)
    # compare(int(text4.get(1.0, "end-1c")),int(text5.get(1.0, "end-1c")))


root = tk.Tk()
root.attributes('-fullscreen', True)
root.title("CSE 5301 - Project - Sorting Algorithms")
frame = tk.Frame(root, bg="#2596be")
frame.place(relheight=1.0, relwidth=1.0, relx=0.0, rely=0.0)
title = tk.Label(frame, text="CSE 5301 - Project - Sorting Algorithms",
                 fg="black", bg="#2596be", font=("Comic Sans MS", 30, "bold"))
title.place(relx=0.25, rely=0.05)

label1 = tk.Label(frame, text="ENTER THE INPUT SIZE OF THE LIST",  padx=10, pady=10,
                  fg="black", bg="#33E6FF", font=("Gill Sans MT", 12))
label1.place(relx=0.1, rely=0.2)
text1 = tk.Text(frame, height=1, width=40, padx=10, pady=10,
                bg="white", fg="black", font=("Gill Sans MT", 12))
text1.place(relx=0.1, rely=0.3)

label2 = tk.Label(frame, text="SORTED ARRAY LIST :",  padx=10,
                  pady=10, fg="black", bg="#33E6FF", font=("Gill Sans MT", 12))
label2.place(relx=0.1, rely=0.4)
text2 = tk.Text(frame, height=1, width=40, padx=10, pady=10,
                bg="white", fg="black", font=("Gill Sans MT", 12))
text2.place(relx=0.1, rely=0.5)

label3 = tk.Label(frame, text="Sorting Algorithm Run Time",  padx=10,
                  pady=10, fg="black", bg="#33E6FF", font=("Gill Sans MT", 12))
label3.place(relx=0.1, rely=0.6)
text3 = tk.Text(frame, height=4, width=40, padx=10, pady=10,
                bg="white", fg="black", font=("Gill Sans MT", 12))
text3.place(relx=0.1, rely=0.7)

bubble_Sort = tk.Button(frame, text="BUBBLE SORT", width=10, padx=20, pady=10, bg="black",
                        fg="black", command=lambda: bubble_sort(inputList), font=("Gill Sans MT", 10))
bubble_Sort.place(rely=0.2, relx=0.3)

insert_Sort = tk.Button(frame, text="INSERTION SORT", width=10, padx=20, pady=10, bg="black",
                        fg="black", command=lambda: insertSort(inputList), font=("Gill Sans MT", 10))
insert_Sort.place(rely=0.2, relx=0.4)

select_Sort = tk.Button(frame, text="SELECTION SORT", width=10, padx=20, pady=10, bg="black",
                        fg="black", command=lambda: selectSort(inputList), font=("Gill Sans MT", 10))
select_Sort.place(rely=0.2, relx=0.5)

heap_sort = tk.Button(frame, text="HEAP SORT", width=10, padx=20, pady=10, bg="black",
                      fg="black", command=lambda: heap_Sort(inputList), font=("Gill Sans MT", 10))
heap_sort.place(rely=0.2, relx=0.6)

quick_sort = tk.Button(frame, text="QUICK SORT", width=10, padx=20, pady=10, bg="black",
                       fg="black", command=lambda: quick_Sort(inputList), font=("Gill Sans MT", 10))
quick_sort.place(rely=0.2, relx=0.7)

threeWayQuick_sort = tk.Button(frame, text="3 WAY QUICK SORT", width=10, padx=20, pady=10,
                               bg="black", fg="black", command=lambda: quickSort_3Way(inputList), font=("Gill Sans MT", 10))
threeWayQuick_sort.place(rely=0.2, relx=0.8)

merge_sort = tk.Button(frame, text="mergeSort", width=10, padx=20, pady=10, bg="black",
                       fg="black", command=lambda: merge_Sort(inputList), font=("Gill Sans MT", 10))
merge_sort.place(rely=0.2, relx=0.9)


label4 = tk.Label(frame, text="Enter a Minimum Size of an Array :",
                  padx=10, pady=10, fg="black", bg="white", font=("Gill Sans MT", 12))
label4.place(relx=0.6, rely=0.45)

label5 = tk.Label(frame, text="Enter a Maximum size of an Array :",
                  padx=10, pady=10, fg="black", bg="white", font=("Gill Sans MT", 12))
label5.place(relx=0.8, rely=0.45)

label6 = tk.Label(frame, text="Run time comparision of algorithms",
                  padx=10, pady=10, fg="black", bg="white", font=("Gill Sans MT", 12), justify="center")
label6.place(relx=0.5875, rely=0.35)

text4 = tk.Text(frame, height=1, width=20, padx=10, pady=10,
                bg="white", fg="black", font=("Gill Sans MT", 10))
text4.place(relx=0.6, rely=0.55)

text5 = tk.Text(frame, height=1, width=20, padx=10, pady=10,
                bg="white", fg="black", font=("Gill Sans MT", 10))
text5.place(relx=0.8, rely=0.55)

text6 = tk.Text(frame, height=1, width=60, padx=10, pady=10,
                bg="white", fg="black", font=("Gill Sans MT", 10))
text6.place(relx=0.6, rely=0.75)

comp = tk.Button(frame, text="COMPARE", width=20, padx=20, pady=10,
                 bg="white", fg="black", command=runTimeComp, font=("Gill Sans MT", 10))
comp.place(rely=0.65, relx=0.7)


root.mainloop()

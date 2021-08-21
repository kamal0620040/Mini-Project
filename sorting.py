# Selection sort algorithm
def selectionSort(arr):  
    for i in range(len(arr)):
        current = i
        for j in range(i+1, len(arr)):
            if arr[current] > arr[j]:
                current = j
           
        arr[i], arr[current] = arr[current], arr[i]

# Bubble sort algorithm
def bubbleSort(arr):
    size = len(arr)
    for i in range(size):
        for j in range(0, size-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
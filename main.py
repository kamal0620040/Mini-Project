import os
import time
from sorting import selectionSort,bubbleSort
import matplotlib.pyplot as plt
from pathlib import Path

# File path For the different directory
BASE_DIR = Path(__file__).resolve().parent
INPUT_DIR = BASE_DIR.joinpath('Input')
OUTPUT_DIR = BASE_DIR.joinpath('Output')

sampleDataSize,selectionSortTimes,bubbleSortTimes,fileName = [],[],[],[]

# Look for the files present in Input folder and extract the file name
for filename in sorted(os.listdir(INPUT_DIR)):
    if filename.endswith(".txt"):
        fileName.append(filename)

# Generate the dataset size from the number present in the filename(i.e 100 if filename is Input-100.txt)
for i in fileName:
    sampleDataSize.append(int(i[6:-4]))
sampleDataSize.sort()

'''
Iterate throgh all the files present in the Input folder.
For each file, extract the data inside it and sore it in list
               short the list using selection and bubble sort and calculate it's execution time
               store the result in the output folder
'''
for filename in sampleDataSize:
    arr = []
    with open(INPUT_DIR.joinpath('Input-'+str(filename)+'.txt'),'r') as file:
        for line in file:
            arr.append(int(line[::-1]))
    arr1 = arr.copy()
    arr2 = arr.copy()
    start = time.time()
    selectionSort(arr1);
    end = time.time()
    selectionSortTimes.append(end-start)
    start = time.time()
    bubbleSort(arr2);
    end = time.time()
    bubbleSortTimes.append(end-start)
    with open(OUTPUT_DIR.joinpath('Selection Sort Output').joinpath('Output-'+str(filename)+'.txt'), "w") as file:
        for i in arr1:
            line = str(i) + '\n'
            file.write(line)
    with open(OUTPUT_DIR.joinpath('Bubble Sort Output').joinpath('Output-'+str(filename)+'.txt'), "w") as file:
        for i in arr2:
            line = str(i) + '\n'
            file.write(line)

print("Data Size:- ",sampleDataSize)
print("Selection Sort Time::")
print(selectionSortTimes)
print("Bubble Sort Time::")
print(bubbleSortTimes)

# Generating graph using matplotlib
plt.xlabel('Dataset Size')
plt.ylabel('Time Complexity')
plt.plot(sampleDataSize, selectionSortTimes, label ='Selection Sort')
plt.plot(sampleDataSize, bubbleSortTimes, label ='Bubble Sort')
plt.grid()
plt.legend()
plt.show()

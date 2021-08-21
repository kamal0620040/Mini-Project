import os
import csv
from pathlib import Path
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent
data_list = []
fileName = []
sampleDataSize = [50,100,250,500,1000,1500,3000,5000,10000]
for filename in sorted(os.listdir(BASE_DIR)):
    if filename.endswith(".csv"):
        fileName.append(filename)
print(fileName)

randomSelectionSortTimes = []
randomBubbleSortTimes = []
sortedSelectionSortTimes = []
sortedBubbleSortTimes = []
reverseSelectionSortTimes = []
reverseBubbleSortTimes = []

for name in fileName:
    with open(name) as f:
        reader = csv.reader(f)
        data_list = list(reader)
        if name[:-4] == 'Sorted':
            for i in data_list[1::]:
                count = 0
                for j in i[1::]:
                    if count == 0:
                        sortedSelectionSortTimes.append(float(j))
                    if count == 1:
                        sortedBubbleSortTimes.append(float(j))
                    count = count + 1
        elif name[:-4] == 'Random':
            for i in data_list[1::]:
                count = 0
                for j in i[1::]:
                    if count == 0:
                        randomSelectionSortTimes.append(float(j))
                    if count == 1:
                        randomBubbleSortTimes.append(float(j))
                    count = count + 1
        elif name[:-4] == 'Reverse':
            for i in data_list[1::]:
                count = 0
                for j in i[1::]:
                    if count == 0:
                        reverseSelectionSortTimes.append(float(j))
                    if count == 1:
                        reverseBubbleSortTimes.append(float(j))
                    count = count + 1

# Generating graph using matplotlib
plt.xlabel('Dataset Size')
plt.ylabel('Time Complexity')
plt.plot(sampleDataSize, randomSelectionSortTimes,'r--', label ='Random Selection Sort')
plt.plot(sampleDataSize, randomBubbleSortTimes,'b--', label ='Random Bubble Sort')
plt.plot(sampleDataSize, sortedSelectionSortTimes,'r',marker='*', label ='Sorted Selection Sort')
plt.plot(sampleDataSize, sortedBubbleSortTimes,'b',marker='*', label ='Sorted Bubble Sort')
plt.plot(sampleDataSize, reverseSelectionSortTimes,'r', label ='Reverse Selection Sort')
plt.plot(sampleDataSize, reverseBubbleSortTimes,'b', label ='Reverse Bubble Sort')
plt.title('combined-graph')
plt.grid()
plt.legend()
plt.savefig('combined-graph'+'.png')
# plt.show()



print(randomSelectionSortTimes)
print(randomBubbleSortTimes)
                        


        

# print(data_list)
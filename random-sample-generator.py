import random
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
INPUT_DIR = BASE_DIR.joinpath('Input')
OUTPUT_DIR = BASE_DIR.joinpath('Output')

# Generate file with specified size with random data inside of Input folder
sampleSize = int(input("Enter the number of random data to crete::"))
out_file = 'Input-'+str(sampleSize)+'.txt'
data = []
with open(INPUT_DIR.joinpath('Random').joinpath(out_file), "w") as file:
    for i in range(sampleSize):
        randint = random.randint(1, 1000000)
        data.append(randint)
        line = str(randint) + '\n'
        file.write(line)

ans = input("Do you want to create shorted input of random data?(Y or N)")
if ans=='Y':
    temp = data.copy()
    temp.sort()
    with open(INPUT_DIR.joinpath('Sorted').joinpath(out_file), "w") as file:
        for i in temp:
            line = str(i) + '\n'
            file.write(line)

ans = input("Do you want to create reversed sorted input of random data?(Y or N)")
if ans=='Y':
    temp = data.copy()
    temp.sort()
    temp.reverse()
    with open(INPUT_DIR.joinpath('Reverse').joinpath(out_file), "w") as file:
        for i in temp:
            line = str(i) + '\n'
            file.write(line)

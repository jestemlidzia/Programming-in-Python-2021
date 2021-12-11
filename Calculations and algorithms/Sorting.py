import random

def bubbleSort(array):
    length = len(array)
    for i in range(length-1):
        for j in range(0, length-i-1):
            if array[j] < array[j + 1] :
                array[j], array[j + 1] = array[j + 1], array[j]

numbers = [random.randrange(100) for i in range(1, 51)]
temp = numbers.copy()

bubbleSort(numbers)
temp.sort(reverse=True)

if(numbers == temp):
    print(numbers)
else:
    print("Not sorted")
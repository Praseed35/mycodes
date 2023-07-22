def bubbleSort(array):
    
    for a in range(len(array)):
    
        for b in range(0, len(array) - a - 1):
        
            if array[b] > array[b + 1]:
        
                temp = array[b]
                array[b] = array[b + 1]
                array[b + 1] = temp

numbers = input("Enter a list of numbers (space-separated): ").split()

array = [int(num) for num in numbers]
print("The original array is:", array)

bubbleSort(array)
print("The Sorted Array is:", array)

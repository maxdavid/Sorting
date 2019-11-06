# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(len(arr)):
        smallest_index = i
        for j in range(i, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j
        arr.insert(i, arr.pop(smallest_index))
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    while True:
        swaps = 0
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr.insert(i, arr.pop(i + 1))
                swaps += 1
        if swaps == 0:
            break
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    output = [0 for i in arr]
    count = [0 for i in arr]
    for num in arr:
        count[num - 1] += 1
    total = 0
    for i in range(len(count)):
        total += count[i]
        count[i] = total

    for num in arr:
        output[count[num - 1] - 1] = num
        count[num - 1] -= 1

    return output


print(count_sort([1, 4, 1, 2, 7, 5, 2]))

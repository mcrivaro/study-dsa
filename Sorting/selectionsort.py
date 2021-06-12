def selection_sort(arr):
    length = len(arr)
    for i in range(0, length):
        index_smallest_val = i
        for j in range(i, length):
            if arr[j] < arr[index_smallest_val]:
                index_smallest_val = j
    temp = arr[i]
    arr[i] = arr[index_smallest_val]
    arr[index_smallest_val] = temp


arr = [6, 2, 10, -1, 5004, 1, 20, 200, 50, 1, 67, 3, 5, 45, 67, 99, 112, 515]
selection_sort(arr)
print(arr)

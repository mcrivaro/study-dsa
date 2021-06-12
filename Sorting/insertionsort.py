def insertion_sort(arr):
    length = len(arr)
    for i in range(0, length-1):
        if arr[i] > arr[i+1]:
            insertion_index = i
            unsorted_num_index = i+1
            for j in range(i, -1, -1):
                if arr[j] < arr[unsorted_num_index]:
                    break
                insertion_index = j
            arr.insert(insertion_index, arr.pop(unsorted_num_index))


def insertion_sort2(arr):
    for i in range(0, len(arr)-1):  # 0
        insertion_index = i+1  # 1
        unsorted_num = arr[insertion_index]  # 2
        while insertion_index > 0 and unsorted_num < arr[insertion_index-1]:
            arr[insertion_index] = arr[insertion_index-1]  # [-1,1,2,6,10,20,5004]
            insertion_index -= 1
        arr[insertion_index] = unsorted_num


arr = [6, 2, 10, -1, 5004, 1, 20, 200, 50, 1, 67, 3, 5, 45, 67, 99, 112, 515]
arr2 = [6, 2, 10, -1, 5004, 1, 20, 200, 50, 1, 67, 3, 5, 45, 67, 99, 112, 515]
insertion_sort2(arr2)
insertion_sort(arr)
print(arr, '\n', arr2)

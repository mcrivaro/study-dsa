def bubble_sort(arr):
    sorted_index = len(arr)
    while sorted_index != 0:
        for i in range(0, sorted_index):
            if i < sorted_index-1:
                if arr[i] > arr[i+1]:
                    buf = arr[i+1]
                    arr[i+1] = arr[i]
                    arr[i] = buf
            else:
                sorted_index = i
    return arr


def bubble_sort_2(arr):
    length = len(arr)
    for i in range(0, length):
        for j in range(0, length-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp


arr = [6, 2, 10, -1, 5004, 1, 20, 200, 50, 67, 3, 5, 45, 67, 99, 112, 515]
bubble_sort(arr)
print(arr)

def merge_sorted_arrays(*arrays):
    # check input (length, format off array, values of array items)
    merged_array = []
    for array in arrays:
        for i in array:
            merged_array.append(i)
    merged_array = sorted(merged_array)
    return(merged_array)


def merge_sorted_arrays2(arr1, arr2): return sorted([*arr1, *arr2])


def merge_sorted_arrays3(arr1, arr2):
    merged_array = []
    if (type(arr1) is not list and type(arr2) is not list):
        return "no arrays given"
    if not (arr1 or arr2):
        len1, len2 = len(arr1), len(arr2)
        return "empty arrays"
    # for i in range(0, len())


if __name__ == "__main__":
    new_array = merge_sorted_arrays([0, 3, 4, 31], [4, 6, 30])
    new_array2 = merge_sorted_arrays2([0, 3, 4, 31], [4, 6, 30])
    new_array3 = merge_sorted_arrays3([0, 3, 4, 31], [4, 6, 30])
    new_array3 = merge_sorted_arrays3([0, 3, 4, 31], [4, 6, 30])
    # print(new_array)
    # print(new_array2)
    print(new_array3)

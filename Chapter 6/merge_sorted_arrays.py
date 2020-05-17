def merge_sorted_arrays(*arrays):
    # check input (length, format off array, values of array items)
    merged_array = []
    for array in arrays:
        for i in array:
            merged_array.append(i)
    merged_array = sorted(merged_array)
    return(merged_array)


def merge_sorted_arrays2(arr1, arr2): return sorted([*arr1, *arr2])

# First two solutions are suboptimal, because they sort the array again. slow


def merge_sorted_arrays3(arr1, arr2):
    merged_array = []
    len1 = len2 = 0
    if (type(arr1) is not list and type(arr2) is not list):
        return "no arrays given"
    else:
        len1, len2 = len(arr1), len(arr2)
    if not (arr1 or arr2):
        return "empty arrays"
    item1 = arr1[0]
    item2 = arr2[0]
    while (len1 or len2):
        if(not len1):
            merged_array.append(*arr2)
            return merged_array
        if(not len2):
            merged_array.append(*arr1)
            return merged_array
        if item1 <= item2:
            merged_array.append(item1)
            if len1 > 1:
                item1 = arr1[1]
            if len1:
                del arr1[0]
                len1 -= 1
        else:
            merged_array.append(item2)
            if len2 > 1:
                item2 = arr2[1]
            if len2:
                del arr2[0]
                len2 -= 1
    return(merged_array)

# solution 3: relatively unclean

#  below given solution in python


def merge_sorted_arrays4(arr1, arr2):
    # check, if valid arrays
    merged_array = []
    if not len(arr1):
        return arr2
    if not len(arr2):
        return arr1
    index_arr1 = 1
    index_arr2 = 1
    arr1_item = arr1[0]
    arr2_item = arr2[0]

    while arr1_item or arr2_item:
        if arr1_item is not None and (arr2_item is None or arr1_item <= arr2_item):
            merged_array.append(arr1_item)
            arr1_item = arr1[index_arr1] if index_arr1 < len(arr1) else None
            index_arr1 += 1
        elif arr2_item is not None and (arr1_item is None or arr1_item >= arr2_item):
            merged_array.append(arr2_item)
            arr2_item = arr2[index_arr2] if index_arr2 < len(arr2) else None
            index_arr2 += 1
    return merged_array


if __name__ == "__main__":
    new_array = merge_sorted_arrays([0, 3, 4, 31], [4, 6, 30])
    new_array2 = merge_sorted_arrays2([0, 3, 4, 31], [4, 6, 30])
    new_array3 = merge_sorted_arrays3([0, 3, 4, 31], [4, 6, 30])
    new_array4 = merge_sorted_arrays4([0, 3, 4, 31], [4, 6, 30])
    print(new_array)
    print(new_array2)
    print(new_array3)
    print(new_array4)

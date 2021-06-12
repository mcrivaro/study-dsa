def reverseStringRec(string_to_reverse, index):
    str_arr = [char for char in string_to_reverse]
    length = len(string_to_reverse)
    limit_val = length/2 if length % 2 == 0 else (length-1)/2
    if index < limit_val:
        buf = str_arr[index]
        str_arr[index] = str_arr[length-1-index]
        str_arr[length-1-index] = buf
        index += 1
        return reverseStringRec(''.join(str_arr), index)
    return ''.join(str_arr)


def reverseStringRec2(string_to_reverse, index):
    str_arr = [char for char in string_to_reverse]
    str_rev = []
    if len(str_arr):
        str_rev.append(str_arr.pop())
    return ''.join(str_rev)


def reverseString(string):
    return reverseStringRec(string, 0)


string = "Hello, World!"
print(reverseString(string))

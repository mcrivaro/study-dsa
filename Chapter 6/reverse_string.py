def split(string):
    my_arr = []
    for char in string:
        my_arr.append(char)
    return my_arr


def reverse_list(char_list):
    reversed_list = []
    for i in range(len(char_list)-1, -1, -1):
        reversed_list.append(char_list[i])
    return reversed_list


def reverse_string(string):
    char_list = split(string)
    reversed_list = reverse_list(char_list)
    str_reversed = ''.join(reversed_list)
    return str_reversed


if __name__ == "__main__":
    test_string = "This is a string."
    str_reversed = reverse_string(test_string)
    print(str_reversed)

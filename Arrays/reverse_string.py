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
    if string and len(string) > 2 and type(string) == str:
        char_list = split(string)
        reversed_list = reverse_list(char_list)
        str_reversed = ''.join(reversed_list)
        return str_reversed
    else:
        return None


def reverse_string1(string):
    if string and len(string) > 2 and type(string) == str:
        char_list = []
        for char in string:
            char_list.append(char)
        reversed_list = []
        for i in range(len(char_list)-1, -1, -1):
            reversed_list.append(char_list[i])
        str_reversed = ''.join(reversed_list)
        return str_reversed
    else:
        return None


def reverse_string2(string):
    if string and len(string) > 2 and type(string) == str:
        reversed_list = []
        for i in range(len(string)-1, -1, -1):
            reversed_list.append(string[i])
        str_reversed = ''.join(reversed_list)
        return str_reversed
    else:
        return None


def reverse_string3(string):
    if string and len(string) > 2 and type(string) == str:
        str_reversed = list(string)
        str_reversed.reverse()
        str_reversed = ''.join(str_reversed)
        return str_reversed
    else:
        return None


if __name__ == "__main__":
    print("Please enter a string:")
    test_string = input()
    str_reversed3 = reverse_string3(test_string)
    print(str_reversed3)

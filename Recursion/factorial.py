def find_factorial_iterative(number):
    counter = 1
    fac = 1
    while (counter <= number):
        fac = fac * counter
        counter += 1
    return fac


def find_factorial_recursive(number):
    if number > 1:
        return number * find_factorial_recursive(number - 1)
    else:
        return 1


def find_factorial_iterative2(number):
    # if you want to save two iterations
    fac = 1
    for i in range(2, number + 1):
        fac = fac * i
    return fac


def find_factorial_recursive2(number):
    # if you want to save two calls
    if number <= 2 and number > 0:
        return number
    elif number <= 0:
        return 1
    else:
        return number * find_factorial_recursive(number - 1)


if __name__ == "__main__":
    for i in range(0, 15 + 1):
        print(f'!{i} = {find_factorial_iterative(i)}')
        print(f'!{i} = {find_factorial_iterative2(i)}')
        print(f'!{i} = {find_factorial_recursive(i)}')
        print(f'!{i} = {find_factorial_recursive2(i)}')
        print('-' * 25)

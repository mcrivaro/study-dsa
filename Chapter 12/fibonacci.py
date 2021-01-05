def fibonacci_iterative(n):
    if n < 2:
        return n
    fib0 = 0
    fib1 = 1
    fib2 = 1
    for _ in range(2, n + 1):
        fib2 = fib1 + fib0
        fib0 = fib1
        fib1 = fib2
    return fib2


def fibonacci_recursive(n):
    if n < 2:
        return n
    else:
        return fibonacci_recursive(n - 2) + fibonacci_recursive(n - 1)


if __name__ == "__main__":
    for i in range(0, 30 + 1):
        print(f'fibonacci({i}) = {fibonacci_iterative(i)}')
        print(f'fibonacci({i}) = {fibonacci_recursive(i)}')
        print('-' * 25)

ARGUMENT_ERROR_MESSAGE ="factorial() takes a positive integer as argument."


def factorial(n):
    if not(isinstance(n, int) or isinstance(n, float)):
        raise TypeError(ARGUMENT_ERROR_MESSAGE)

    if n < 0 or n != int(n):
        raise ValueError(ARGUMENT_ERROR_MESSAGE)

    if n < 2:
        return 1
    
    return n * factorial(n-1)


if __name__ == '__main__':
    pass

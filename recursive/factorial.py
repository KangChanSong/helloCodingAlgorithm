def factorial(i):
    if i == 1:
        return i;
    else:
        return i * factorial(i - 1);


if __name__ == '__main__':
    print(factorial(5))

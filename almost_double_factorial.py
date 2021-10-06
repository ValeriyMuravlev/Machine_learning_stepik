def almost_double_factorial(n):
    if 0 < n <= 100:
        temp = 1
        for i in range(n + 1):
            if i % 2 != 0:
                temp *= i
    elif n == 0:
        return 1

    return  temp
print(almost_double_factorial(9))
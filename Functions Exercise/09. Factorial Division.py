def calc_factorial(n):
    res = 1
    for num in range(1, n + 1):
        res *= num

    return res


num1 = int(input())
num2 = int(input())

factorial_num1 = calc_factorial(num1)
factorial_num2 = calc_factorial(num2)

result = factorial_num1 / factorial_num2
print(f"{result:.2f}")

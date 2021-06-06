from sys import maxsize

num1 = int(input())
num2 = int(input())
num3 = int(input())


def minimum_function():
    minimum_num = maxsize
    if num1 < minimum_num:
        minimum_num = num1
        if num2 < minimum_num:
            minimum_num = num2
            if num3 < minimum_num:
                minimum_num = num3
    print(minimum_num)


minimum_function()

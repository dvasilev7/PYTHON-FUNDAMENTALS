import sys
n = int(input())
even_sum = 0
odd_sum =0
odd_max_element = - sys.maxsize
odd_min_element = sys.maxsize
even_max_element = - sys.maxsize
even_min_element = sys.maxsize
for numbers in range(1, n + 1):
    number = float(input())
    if numbers % 2 == 0:
        even_sum += number
        if number < even_min_element:
            even_min_element = number
        if number > even_max_element:
            even_max_element = number
    else:
        odd_sum += number
        if number < odd_min_element:
            odd_min_element = number
        if number > odd_max_element:
            odd_max_element = number
print(f"OddSum={odd_sum:.2f},")
if odd_min_element != sys.maxsize:
    print(f"OddMin={odd_min_element:.2f},")
else:
    print("OddMin=No,")
if odd_max_element != - sys.maxsize:
    print(f"OddMax={odd_max_element:.2f},")
else:
    print("OddMax=No,")
print(f"EvenSum={even_sum:.2f},")
if even_min_element != sys.maxsize:
    print(f"EvenMin={even_min_element:.2f},")
else:
    print("EvenMin=No,")
if even_max_element != - sys.maxsize:
    print(f"EvenMax={even_max_element:.2f}")
else:
    print("EvenMax=No")
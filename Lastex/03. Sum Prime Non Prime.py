# променлива за начало "комманда"
# променлива за сума на простите числа (не я занулявам)
# променлова за сума на непростите числа (не я занулявам)

# докато командата е различна от stop
# number = int(command)
# Когато числото е отрицателно:
    # print "Number is negative."
# докато проверката е в диапазона от 2 до числото
    # ако числото е просто (по-голямо от 1 и се дели само на себе си и на 1)
    # събирам числото със сумата на простите числа
    # иначе - не е просто
    # събирам числото съм сумата на непростите числа
# иначе когато командата е stop
    # break
# print "Sum of all prime numbers is: "
# print "Sum of all non prime numbers is: "
sum_prime = 0
sum_non_prime = 0
command = input()
while command != "stop":
    number = int(command)
    is_prime = True
    if number < 0:
        print("Number is negative.")
        command = input()
        continue
    for checking in range(2, number):
        if number % checking == 0:
            is_prime = False
            break
    if is_prime:
        sum_prime += number
    else:
        sum_non_prime += number
    command = input()
print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_non_prime}")



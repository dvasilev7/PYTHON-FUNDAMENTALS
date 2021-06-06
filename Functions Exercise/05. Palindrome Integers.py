def is_palindrome(element):
    reversed_element = element[::-1]
    if element == reversed_element:
        return True
    return False


def separate_elements(element, separator):
    numbers_as_strings = element.split(separator)
    return numbers_as_strings


data = input()
nums_strings = separate_elements(data, ", ")

for el in nums_strings:
    print(is_palindrome(el))
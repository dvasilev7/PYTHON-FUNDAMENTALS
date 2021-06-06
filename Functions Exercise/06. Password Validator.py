def password_validator(password):
    is_password_valid = True
    if not (6 <= len(password) <= 10):
        print("Password must be between 6 and 10 characters")
        is_password_valid = False
    digits_counter = 0
    for el in password:
        if not el.isdigit() and not el.isalpha():
            print("Password must consist only of letters and digits")
            is_password_valid = False
            break
        if el.isdigit():
            digits_counter += 1
    if not digits_counter >= 2:
        print("Password must have at least 2 digits")
        is_password_valid = False
    if is_password_valid:
        print("Password is valid")


pw = input()
password_validator(pw)

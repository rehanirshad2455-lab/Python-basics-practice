def validate_password(password):
    is_upper = False
    is_lower = False
    is_digit = False
    if len(password) >=  8:
        for char in password:
            if char.isupper():
                is_upper = True
            if char.islower():
                is_lower =  True
            if char.isdigit():
                is_digit = True


    if len(password) >= 8 and is_upper and is_lower and is_digit:
        return True
    else:
        return False
            

result = validate_password("Python12")
print(result)


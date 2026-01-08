password = input("Enter the password : ")

digit = False
special = False
special_chars = "*&^%$#@!"
min_length = 8

if len(password) >= min_length:
    for eachchar in password:
        if eachchar.isdigit():
            digit = True
        if eachchar in special_chars:
            special = True
    if digit and special:
        print("Password is valid")
    else:
        if digit:
            print("Password is not valid please include the special characters into it")
        else:
            print("Password is not valid please include the numbers into it")
else:
    print("Password length should be at least 8")
    print("Password length should be greater than 8")

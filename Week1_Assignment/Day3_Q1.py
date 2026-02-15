def factorial(num):
    if num <=1:
        return 1
    return num * factorial(num-1)

x = 5
a = factorial(x)
print("The factorial for the num ", x, "is : ", a)



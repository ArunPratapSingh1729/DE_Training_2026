def fun(num):
    if num <=1:
        return 1
    return num * fun(num-1)

x = 5
a = fun(x)
print("The factorial for the num ", x, "is : ", a)



def function(num):
    if num <= 1:
        return 1
    return num * function(num-1)

x = 5
try:
    a = function(x)
    print("The factorial for the num", x, "is:", a)
except Exception as e:
    print("Exception: ", e)
finally:
    print("your program get run")



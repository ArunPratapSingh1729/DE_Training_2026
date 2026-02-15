def function(func1, func2, value):
    result1 = func1(value)
    result2 = func2(value)
    return (result1, result2)

def double(x):
    return x * 2

def square(x):
    return x * x

output = function(double, square, 5)
print(output)


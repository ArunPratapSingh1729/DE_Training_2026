def outer(x):
 
    def inner(y):
        return x + y  

    return inner

output = outer(10)

print(output(20))


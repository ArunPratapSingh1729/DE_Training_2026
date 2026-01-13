l = [1,2,3,4,5]
x  = list(map(lambda x : (x + 10) , l))
x = list(map(lambda y : y*y , x))

print(x)
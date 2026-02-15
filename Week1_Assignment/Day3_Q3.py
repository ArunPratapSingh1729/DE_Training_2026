l = [3,1,4,5,6,7,8,2,0,9]

try:
    a = list(map(lambda x : (x+10)**2 , l) )
except Exception as e:
    print("Exception: ", e)

print(a)
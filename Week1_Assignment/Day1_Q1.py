a = 5
b = 10

c = "arun"
d = "pratap"
# i use tuple unpacking here as it works for the integer as well as
# for the strings 
a,b  = b,a 

print("a == ",a)
print("b == ",b)

c,d = d,c

print(c)
print(d)
text = "hello world"

ch={}

for i in text:
    if i in ch:
        ch[i] += 1
    else:
        ch[i] = 1

print(ch)

#lambda expression
# string = "arun"
# a = list(map(lambda x : string.count(x), string))
# d = {i:string.count(i) for i in string}
# print(a)
# print(d)
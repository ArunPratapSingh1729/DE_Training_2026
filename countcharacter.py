text = "hello world"

ch={}

for i in text:
    if i in ch:
        ch[i] += 1
    else:
        ch[i] = 1

print(ch)
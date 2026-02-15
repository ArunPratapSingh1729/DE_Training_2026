def generator(limit):
    for i in range(1, limit + 1):
        yield i * i

for square in generator(5):
    print(square)


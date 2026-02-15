class numberiterator:
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.numbers):
            value = self.numbers[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration

nums = numberiterator([1, 2, 3, 4])

for num in nums:
    print(num)

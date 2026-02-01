from itertools import permutations

def validator(fn):
    def inner(arr):
        res = []
        for p in fn(arr):
            mid = len(p) // 2
            if p[mid] ** 2 > sum(p) - p[mid]:
                res.append(list(p))
        return res
    return inner

@validator
def valid_permutations(arr):
    return set(permutations(arr))
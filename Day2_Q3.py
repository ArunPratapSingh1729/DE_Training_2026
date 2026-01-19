data = {
    "apple": 10,
    "banana": 20,
    "avocado": 15,
    "Apricot": 25,
    "grape": 30
}

dic = {k:v for k,v in data.items() if k.lower().startswith('a')}
print(dic)


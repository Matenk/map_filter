collection = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]

def multi(x):
    return x ** 2

def odd_number(x):
    return x % 2

new_collection = map(multi, filter(odd_number, collection))

print(list(new_collection))

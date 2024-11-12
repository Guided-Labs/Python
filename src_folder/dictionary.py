## Creation

D = {'name': 'John', 'age': 25, 'city': 'New York'}
print(D)


## Accessing / Indexing

# D = {'name': 'John', 'age': 25, 'city': 'New York'}
# print(D['name'])


## Modifying Values

# D = {'name': 'John', 'age': 25, 'city': 'New York'}
# D['age'] = 30
# print(D)


## Adding New Key-Value Pairs

# D = {'name': 'John', 'age': 25, 'city': 'New York'}
# D['job'] = 'Engineer'
# print(D)


## Dictionary Methods

## get()

# D = {'name': 'John', 'age': 30, 'city': 'New York', 'job': 'Engineer'}
# job = D.get('job')
# print(job)


## keys()

# D = {'name': 'John', 'age': 30, 'city': 'New York', 'job': 'Engineer'}
# keys = D.keys()
# print(keys)

##  values()

# D = {'name': 'John', 'age': 30, 'city': 'New York', 'job': 'Engineer'}
# values = D.values()
# print(values)


## items()

# D = {'name': 'John', 'age': 30, 'city': 'New York', 'job': 'Engineer'}
# items = D.items()
# print(items)


## copy()

# D = {'name': 'John', 'age': 30, 'city': 'New York', 'job': 'Engineer'}
# D_copy = D.copy()
# print(D_copy)


## pop()

# D = {'name': 'John', 'age': 30, 'city': 'New York', 'job': 'Engineer'}
# job = D.pop('job')
# print(job)
# print(D)


## popitem()

# D = {'name': 'John', 'age': 30, 'city': 'New York'}
# item = D.popitem()
# print(item)
# print(D)


## update()

# D = {'name': 'John', 'age': 30, 'city': 'New York'}
# D.update({'age': 35, 'city': 'Boston'})
# print(D)


## clear()

# D = {'name': 'John', 'age': 35, 'city': 'Boston'}
# D.clear()
# print(D)


## Checking for Existence of Keys

# D = {'age': 35, 'city': 'Boston'}
# if 'name' in D:
#  print("Key exists")
# else:
#  print("Key does not exist")


## Dictionary Comprehension

# squares = {x: x**2 for x in range(5)}
# print(squares)

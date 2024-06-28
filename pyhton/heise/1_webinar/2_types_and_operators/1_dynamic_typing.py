g = 'Hello!'
print('ID of g:', id(g))
print('Type of g:', type(g))
print('Value of g:', g)

print('-' * 100)

g = 9904
print('ID of g:', id(g))
print('Type of g:', type(g))
print('Value of g:', g)

print('-' * 100)

b = 9904
print('ID of b:', id(b))
print('Type of b:', type(b))
print('Value of b:', b)

print('-' * 100)

print('g is b:', g is b)
print('type(g) == type(b):', type(g) == type(b))
print('g == b:', g == b)

print('-' * 100)

b += 1
print('g is b:', g is b)
print('type(g) == type(b):', type(g) == type(b))
print('g == b:', g == b)
print(f'{g=} {b=}')

print('-' * 100)

b -= 1
print('g is b:', g is b)
print('type(g) == type(b):', type(g) == type(b))
print('g == b:', g == b)
print(f'{g=} {b=}')


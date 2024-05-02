u = [2155, 9550, None, 68.90, 51.36, False, 'p', 'n', True, [9, 0, 7, 2]]
print(u)
print(type(u))
print(u[5])
for n in u:
    print(n)

print('-' * 100)

v = list('Data')
print(v)
v += 'Structures'
print(v)
v.insert(4, ' ')
print(v)
v.append('!')
print(v)

print('-' * 100)

v.remove(' ')
print(v)
del v[-1]
print(v)

print('-' * 100)

v.reverse()
print(v)
w = sorted(v)
print(v, w)
v.sort()
print(v)
v.sort(key=str.lower)
print(v)
v.sort(key=str.lower, reverse=True)
print(v)

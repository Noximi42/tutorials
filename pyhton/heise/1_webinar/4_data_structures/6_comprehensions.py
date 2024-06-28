import math

square_numbers = [i * i for i in range(1, 10 + 1)]
print(square_numbers)

print('-' * 100)

even_square_roots = (math.sqrt(i) for i in square_numbers if i % 2 == 0)
print(even_square_roots)
print(tuple(even_square_roots))

print('-' * 100)

# dictionary of number / cube number pairs
cube_number_dict = {i: i ** 3 for i in range(-5, 5 + 1)}
print(cube_number_dict)
for k in cube_number_dict:
    print(f'{k:2} | {cube_number_dict[k]:4}')

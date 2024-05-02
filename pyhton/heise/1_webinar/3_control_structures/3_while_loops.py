I_SQUARED_MAX = 1_000_000

i = 1
i_squared = i * i
while i_squared <= I_SQUARED_MAX:
    print(f'{i:4}^2 = {i_squared:7}')
    if str(i_squared).count('6') >= 3:  # stop if i^2 contains at least three 6 digits.
        break
    i += 1
    i_squared = i * i
else:
    print('Maximum reached.')

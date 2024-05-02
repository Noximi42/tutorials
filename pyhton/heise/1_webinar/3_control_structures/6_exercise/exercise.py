A_MAX = 9
B_MAX = 9

for a in range(1, A_MAX + 1):
    for b in range(1, B_MAX + 1):
        print(f'{a} \N{multiplication sign} {b} = {(a * b):2}    ', end='')
    print()

print('-' * 100)

if A_MAX <= 0:
    print('"A_MAX" must be positive.')
elif B_MAX <= 0:
    print('"B_MAX" must be positive.')
else:
    a_length = len(str(A_MAX))
    b_length = len(str(B_MAX))
    axb_length = len(str(A_MAX * B_MAX))
    for a in range(1, A_MAX + 1):
        for b in range(1, B_MAX + 1):
            print(f'{a:{a_length}} \N{multiplication sign} {b:{b_length}} = {(a * b):{axb_length}}    ', end='')
        print()

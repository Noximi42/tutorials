def ab_plus_c(a, b, c):
    print(f"{a=} | {b=} | {c=}")
    return a * b + c


print(ab_plus_c(7, 8, 2))
print()
print(ab_plus_c(8, 3, 11))
print()
print(ab_plus_c(2, c=5, b=7))

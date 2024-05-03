def ab_plus_c(a, b=1, c=0):
    print(f"{a=} | {b=} | {c=}")
    return a * b + c


def calculate(a, b, c, method="ab_plus_c"):
    print(f"{a=} | {b=} | {c=} | {method=}")
    if method == "ab_plus_c":
        return a * b + c
    elif method == "min":
        return min(a, b, c)
    elif method == "max":
        return max(a, b, c)
    else:
        return None


print(ab_plus_c(a=4, b=8, c=7))
print()
print(ab_plus_c(c=10, a=7))
print()
print(ab_plus_c(2, b=7))

print("-" * 100)

print(calculate(14, 13, 6))
print()
print(calculate(14, 13, 6, method="min"))
print()
print(calculate(14, 13, 6, method="max"))
print()

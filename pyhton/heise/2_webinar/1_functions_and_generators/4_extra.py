def calculate(method="ab_plus_c", *values):
    print(f"{method=} | {values=}")
    if method == "ab_plus_c":
        return values[0] * values[1] + values[2]
    elif method == "min":
        return min(values)
    elif method == "max":
        return max(values)
    else:
        return None


print(calculate(8, 2, 18))  # wrong 8 is method in this case
print()
print(calculate("ab_plus_c", 8, 2, 18))
print()
print(calculate("max", list(range(1, 10 + 1))))  # wrong (need to spread this)
print()
print(calculate("max", *list(range(1, 10 + 1))))

h = 5800
r = 3338
p = 1823
w = h > r > p
print(w, type(w))

print(bool(h))

print(bool(0))

print(h > r and r > p)  # warning

print("-" * 100)

if "":
    print("Empty string is true")

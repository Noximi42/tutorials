a = ["f", "g", "h", "i", 3, 4, 5, 6, [7, "v"]]
print(a)
print(a[1:5])
print(a[:-1])
print(a[::2])
print(a[5:0:-1])
print(a[-1][1])

print("-" * 100)

c = "0123456789012345"
f = "Slicing is cool!"
print(c)
print(f)
print(f[11:15])
print(f[:10])
print(f[:-1])
print(f[::-1])
print(f[14::-2])

print("-" * 100)

print(a)
a[3] = "j"
print(a)
a[4:8] = [1, 2, 3, 4]
print(a)

print("-" * 100)

print(f[6:5])

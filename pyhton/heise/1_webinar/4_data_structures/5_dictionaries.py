chancellors = {"Gerhard": (1998, 2005), "Angela": (2005, 2021)}
print(chancellors["Angela"])

chancellors["Olaf"] = (2021, 9999)
print(chancellors["Olaf"])

print()

for k in chancellors.keys():
    print(k)

print()

for i in chancellors.items():
    print(i)

print()

for v in chancellors.values():
    print(v)

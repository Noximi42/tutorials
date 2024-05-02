A_MAX = input("Enter first number: ")
B_MAX = input("Enter second number: ")

try:
    A_MAX = int(A_MAX)
except Exception as e:
    print("Enter a valid number")
    exit()

try:
    B_MAX = int(B_MAX)
except Exception as e:
    print("Enter a valid number")
    exit()

A_MAX = int(A_MAX)
B_MAX = int(B_MAX)

if A_MAX <= 0 or B_MAX <= 0:
    print("Olny positive numbers allowed")
    exit()


for i in range(1, A_MAX + 1):
    for j in range(1, B_MAX + 1):
        result = i * j
        print(f"{i} \N{MULTIPLICATION SIGN} {j} = {result:2} \t", end="")
    print("")

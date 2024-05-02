year = 2024

if year % 400 == 0:
    leap_year = True
elif year % 100 == 0:
    leap_year = False
elif year % 4 == 0:
    leap_year = True
else:
    leap_year = False

print(f'{year}', 'IS a leap year.' if leap_year else 'is NOT a leap year.')

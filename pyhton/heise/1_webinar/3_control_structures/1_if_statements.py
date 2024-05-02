year = 2024

if year % 400 == 0:
    leap_year = True
elif year % 100 == 0:
    leap_year = False
elif year % 4 == 0:
    leap_year = True
else:
    leap_year = False

if leap_year:  # "leap_year" is also available outside the if statement.
    print(f'{year} IS a leap year.')
else:
    print(f'{year} is NOT a leap year.')

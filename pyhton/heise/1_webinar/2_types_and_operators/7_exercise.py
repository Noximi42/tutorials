numerator_string = input('Numerator: ')
if not (5 <= len(numerator_string) <= 8):
    print('The numerator must consist of 5 to 8 digits.')
    exit()
numerator = int(numerator_string)

denominator_string = input('Denominator: ')
if not (2 <= len(denominator_string) <= 5):
    print('The denominator must consist of 2 to 5 digits.')
    exit()
denominator = int(denominator_string)

result = numerator / denominator
print(f'{numerator} / {denominator} = {result:.3f}')

letters = set('abcdefghijklmnopqrstuvwxyz')
print(letters)
letters.add('ß')
print(letters)

vowel_letters = {'a', 'ä', 'e', 'i', 'o', 'ö', 'u', 'ü', 'y'}
print(vowel_letters)

print()

print('Subset?', vowel_letters <= letters)
print('Union:', letters | vowel_letters)
print('Intersection:', letters & vowel_letters)
print('Difference:', letters - vowel_letters)
print('Symmetric difference:', letters ^ vowel_letters)
print('Symmetric difference:', sorted(letters ^ vowel_letters))

print()

letters.remove('ß')
print(letters)

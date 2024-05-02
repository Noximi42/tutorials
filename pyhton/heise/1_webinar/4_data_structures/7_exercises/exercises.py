text = 'Data Structures, Slicing, and Comprehensions'
vowel_list = [letter for letter in text if letter in 'aeiou']
vowel_string = ''.join(vowel_list)
print(vowel_string)

print('-' * 100)

text1 = 'Data Structures'
text2 = 'Slicing'
text3 = 'Comprehensions'
text1_set = set(text1.lower())
text2_set = set(text2.lower())
text3_set = set(text3.lower())
print(text1_set & text2_set & text3_set)

print('-' * 100)

long_text = """Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.[32]
Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.[33][34]
Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language and first released it in 1991 as Python 0.9.0.[35] Python 2.0 was released in 2000 and introduced new features such as list comprehensions, cycle-detecting garbage collection, reference counting, and Unicode support. Python 3.0, released in 2008, was a major revision that is not completely backward-compatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020.[36]
Python consistently ranks as one of the most popular programming languages.[37][38][39][40]
"""  # source: en.wikipedia.org/wiki/Python_(programming_language)
long_text = long_text.replace('\n', ' ')
word_list = long_text.split(' ')
word_length_dict = {word: len(word) for word in word_list}
max_word_length = max(word_length_dict.values())
for current_word in sorted(word_length_dict):
    print(f'{current_word:{max_word_length}} | {word_length_dict[current_word]}')

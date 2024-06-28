text = "Data Structures, Slicing, and Comprehensions"
vowels = "aeiou"

result = [l for l in text if l in vowels]
result = "".join(result)
print(result)

print("-" * 100)

text1 = "Data Structures"
text2 = "Slicing"
text3 = "Comprehensions"

long_text = """Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.[32]
Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.[33][34]
Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language and first released it in 1991 as Python 0.9.0.[35] Python 2.0 was released in 2000 and introduced new features such as list comprehensions, cycle-detecting garbage collection, reference counting, and Unicode support. Python 3.0, released in 2008, was a major revision that is not completely backward-compatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020.[36]
Python consistently ranks as one of the most popular programming languages.[37][38][39][40]
"""

long_text = long_text.replace("\n", "")
words = long_text.split(" ")

dic = {w: len(w) for w in words}
max_length = max(dic.values())

sorted_list = list(dic)
# sorted_list.sort(key=str.lower)
sorted_list = sorted(sorted_list, key=str.lower)

for key in sorted_list:
    print(f"{key:{max_length}}| {dic[key]}")

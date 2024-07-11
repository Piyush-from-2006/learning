'''Write a script in Python to count the total number of vowels and total
Number of consonants present in a file "POEM.TXT".'''
filename = "POEM.TXT"
vowels = "AEIOUaeiou"
with open(filename, 'r') as file:
    content = file.read()
    vowel_count = 0
    consonant_count = 0
    for char in content:
        if char in vowels:
            vowel_count += 1
        elif char.isalpha():
            consonant_count += 1
    print('vowel count',vowel_count)
    print('consonant count',consonant_count)

def count_vowels(word):
    vowels = "aeiouAEIOU"
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count

word = input("Enter a word: ")
num_vowels = count_vowels(word)
print(f"The number of vowels in '{word}' is: {num_vowels}")

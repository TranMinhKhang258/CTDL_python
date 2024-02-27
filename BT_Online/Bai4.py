def are_anagrams(word1, word2):
    clean_word1 = ''.join(word1.split()).lower()
    clean_word2 = ''.join(word2.split()).lower()

    return sorted(clean_word1) == sorted(clean_word2)

word1 = "restful"
word2 = "fluster"
result = are_anagrams(word1, word2)

if result:
    print(f"{word1} and {word2} are anagrams.")
else:
    print(f"{word1} and {word2} are not anagrams.")

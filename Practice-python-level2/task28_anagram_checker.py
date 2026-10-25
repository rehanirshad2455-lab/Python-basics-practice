def anagram_check(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    if sorted(word1) == sorted(word2):
        return True
    else:
        return False


result = anagram_check("list", "litt")
print(result)
# The sec about strings like they will give u a word (hate)
# N a list of words, u will count how many vowel letters
# in hate and then return the word in the list which has the same n of vowel words


# you can iterate over string
def vowels(string, list):
    vowelslist = ["a", "e", "i", "o", "u"]
    vowelsinstring = 0
    wordstoreturn = []
    for chr in string:
        if chr in vowelslist:
            vowelsinstring += 1
    for word in list:
        vowelsinword = 0
        for chr in word:
            if chr in vowelslist:
                vowelsinword += 1
        if vowelsinword == vowelsinstring:
            wordstoreturn.append(word)
    return wordstoreturn


print(vowels("Hate", ["kate", "lips", "Fate"]))

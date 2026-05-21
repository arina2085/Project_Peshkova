def sortWordsByLength():
    words = str(input("Введите строку: "))
    words2 = words.split()
    words3 = sorted(words2, key = lambda word: len(word))

    return ' '.join(map(str, words3))

print(sortWordsByLength())

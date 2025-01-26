
numbers = [2, 53, 19, 39, 28, 40, 69]
numbers40 = list(filter(lambda num: num >= 40, numbers))
print(numbers40)

numbers2 = [5, 23, 49, 19, 48, 20, 72]
numberssquare = list(map(lambda x: x ** 2, numbers2))
print(numberssquare)

words = ["ana, ali, sandro, liza, jumber, zura"]
wordsa = list(filter(lambda word: word.endswith('a'), words))
print(wordsa)

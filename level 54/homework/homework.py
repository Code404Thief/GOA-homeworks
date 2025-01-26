# 2
numbers = [2,4,6,8,10]
twice_numbers = list(map(lambda x: x*2, numbers))
print(twice_numbers)
# 3
names = ["alice", "bob", "charlie"]
result1 = list(map(lambda y: "hello, " + y, names))
print(result1)
# 4
fruits = ["apple", "banana", "kiwi"]
lengths = list(map(len, fruits))
print(lengths)
# 5
numbers1 = [-5, 3, -2, 7, 0, 10]
result2 = list(filter(lambda x: x>= 0, numbers1))
print(result2)
# 6
words = ["pear", "apple", "peach", "grape"]
wordsp = list(filter(lambda word: word.startswith('p'), words))
print(wordsp)
# 7
numbers = [10, 55, 42, 78, 65, 20]
numbers50 = list(filter(lambda num: num > 50, numbers))
print(numbers50)


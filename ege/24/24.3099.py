from collections import Counter


f = open('24-157.txt')
letterFrequencies = Counter(f.read()).most_common()
countOfLettersWithOddFrequency = 0
for letter in letterFrequencies:
    if letter[1] % 2 == 1:
        countOfLettersWithOddFrequency += 1
print(countOfLettersWithOddFrequency // 2)

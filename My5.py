stroka = input()
words = stroka.split()
symbols = sum([len(word) for word in words])
print(round(symbols/len(words),2))
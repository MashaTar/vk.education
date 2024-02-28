# Необходимо написать программу, которая будет принимать на вход строку, разбивать строку на слова по пробелу.
# Далее нужно из всех слов убрать следующие пунктуационные знаки: !,.?;:#$%^&*(),
# а также привести слова к нижнему регистру. В итоге нужно вывести в алфавитном порядке слова,
# которые состоят как минимум из 5 символов, а также имеют как минимум 4 уникальных символа,
# и которые встретились в исходном тексте более 2х раз.

text = input()
punc = '!,.?;:#$%^&*()'
for sym in text:
    if sym in punc:
        text = text.replace(sym, "")

lst = []
for word in text.lower().split():
        lst.append(word)
lst = sorted(lst)

dictionary = dict()
for word in lst:
    if len(word)>=5 and len(set(word))>=4:
       dictionary[word] = dictionary.get(word, 0) + 1
for key, value in dictionary.items():
    if value>2:
       print(key)






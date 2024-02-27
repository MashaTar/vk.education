text = input()
unique = set(text.lower())
char_symbol = " ".join(sorted(unique))
print(char_symbol)

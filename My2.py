a = int(input())
b = int(input())
value = True

while True:
    try:
        c = input()
    except:
        c = ''
    if c == '':
        break
    if value:
        value = a <= int(c) <= b

print(value)
file = 'Alis in Wonderland.txt'

with open(file, encoding='utf-8') as f:
    content = f.read()

print(content.lower().count('the'))
print(content.lower().count('the '))

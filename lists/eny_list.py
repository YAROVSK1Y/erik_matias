
bestes_lang = ['ukrainisch', 'deutsch', 'japanisch', 'spanisch', 'italiwnisch',
               'portugesisch', 'englisch', 'polnisch', 'afrikan']

print(len(bestes_lang))

print(bestes_lang[0].title())
print(bestes_lang[3].title())
print(bestes_lang[-8].title())
print(bestes_lang[-2].title())

bestes_lang[8] = 'cinesisch'
print(bestes_lang)

bestes_lang.append('hindi')
print(bestes_lang)

bestes_lang.insert(9, 'suumi')
print(bestes_lang)

del bestes_lang[10]
print(bestes_lang)
del bestes_lang[4]
print(bestes_lang)
bestes_lang.pop(4)
print(bestes_lang)
bestes_lang.remove('suumi')
print(bestes_lang)
bestes_lang.sort(reverse=True)
print(bestes_lang)
bestes_lang.sort()
bestes_lang.pop()
print(bestes_lang)
bestes_lang.pop()
bestes_lang.pop()
bestes_lang.pop()
bestes_lang.pop()
bestes_lang.pop()
bestes_lang.pop()
print(bestes_lang)
print(bestes_lang)


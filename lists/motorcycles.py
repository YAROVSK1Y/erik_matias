"""""
motorcycles = ['honda', 'yamaha', 'suzuki']

print(motorcycles)

#motorcycles[0] = 'ducati'
motorcycles.append('ducati')

motorcycles_new = []

motorcycles_new.append('java')
motorcycles_new.append('bmw')
motorcycles_new.append('makaka')

print(motorcycles_new)

print(motorcycles)
motorcycles.insert(0, 'harly')
print(motorcycles_new)
print(motorcycles)
motorcycles_new.insert(1, 'ktm')
print(motorcycles_new)

del motorcycles_new[0]
print(motorcycles_new)
del motorcycles_new[1]
print(motorcycles_new)
del motorcycles_new[0]
print(motorcycles_new)
del motorcycles_new[0]
print(motorcycles_new)

motorcycles = ['honda', 'yamaha', 'suzuki']

print(motorcycles)
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']

last_owned = motorcycles.pop(1)
print(f"The last motorcycles I owned was a {last_owned.title()}.")
motorcycles.pop()
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles.remove('suzuki')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']

print(motorcycles)


"""
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_much = 'ducati'
motorcycles.remove(too_much)
print(motorcycles)
print(f"\n Too much motorcycles , {too_much.title()} it`s too much...")

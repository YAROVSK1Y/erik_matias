
def print_metla(lis_m):
    while lis_m:
        readilist = lis_m.pop()
        completed.append(readilist)
    print(f" Ці данні було надіслано\n{completed}")






metllica_Sand = ['No Leaf Clover', 'Master Of Puppets', 'Fuel']
completed = []

print_metla(metllica_Sand[:])
print("Надіслані")
print(completed)
print("Оригінальні")
print(metllica_Sand)

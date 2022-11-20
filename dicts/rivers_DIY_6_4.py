
rivers = {'dnipro':'ukraine', 'rein':'deutschland', 'misisips':'usa'}

for riv, land in rivers.items():
    print(f"The {riv.title()} runs through {land.title()}")

print("===================================")

for riv in rivers.keys():
    print(riv.title())
print("==================================")

for riv in rivers.values():
    print(riv.title())


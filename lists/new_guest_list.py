
guest_list = ['freddie mercury', 'einschtein', 'platon', 'copernik']

guest_list.pop(3)

print(guest_list)

guest_list.insert(1, 'skovoroda')

print(guest_list)
print('I found a bigger table')

guest_list.insert(0, 'schewchenko')
guest_list.insert(2, 'exupery')
guest_list.append('cleopatra')

print(f"I invite you, dear {guest_list[0].title()}\n I invite you, dear {guest_list[1].title()}"
      f"\nI invite you, dear {guest_list[2].title()}\nI invite you, dear {guest_list[3].title()}\n"
      f"I invite you, dear {guest_list[4].title()}\nI invite you, dear {guest_list[5].title()}\n"
      f"I invite you, dear {guest_list[6].title()}.")

print('oops, I think I can only invite two of you...')

print(f"I'm sorry {guest_list[0].title()}, but I can't invite you")
guest_list.pop(0)
print(guest_list)
print(f"I'm sorry {guest_list[1].title()}, but I can't invite you")
guest_list.pop(1)
print(guest_list)
print(f"I'm sorry {guest_list[0]}, but I can't invite you")
guest_list.pop(0)
print(guest_list)
print(f"I'm sorry {guest_list[0].title()}, but I can't invite you")
guest_list.pop(0)
print(guest_list)
print(f"I'm sorry {guest_list[1].title()}, but I can't invite you")
guest_list.pop(1)
print(guest_list)
print(f"And you are invited dear {guest_list[0].title()} !\n"
      f"And you are invited dear {guest_list[1].title()}!")
print('oops...')

del guest_list[0]
del guest_list[0]
print(guest_list)




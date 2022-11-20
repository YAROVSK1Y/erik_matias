file = 'cats.txt'
file_2 = 'dogs.txt'
try:
    with open(file, 'r') as f:
        content = f.read()
    print(f"{content}")
except FileNotFoundError:
    pass

    with open(file_2, 'r') as f_:
        cont = f_.read()
try:
    
    print(cont)
except NameError:
    print("""Ot halepa....
    !!!NameError:!!!""")
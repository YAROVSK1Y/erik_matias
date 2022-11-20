
mans = [{'first_name': 'andrii', 'last_name': 'yar', 'age': '42', 'city': 'krop'},
       {'first_name': 'mikola', 'last_name': 'sed', 'age': '38', 'city': 'krop'},
       {'first_name': 'valera', 'last_name': 'bil', 'age': '46', 'city': 'krop'}]
print("=User= =Nachname=   ")
for man in mans:
    man_info = f"{man['first_name']}:  {man['last_name']}:  {man['age']}:  {man['city']}"
    print(man_info)


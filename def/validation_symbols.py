# перелік допустимих символів
etalon = "0123456789"
# об'єкт що перевіряється
string = "123f"

for i in string:
    if i in etalon:
        print("Oll OK")
    else:
        print("error")


# Приклади перебору словників

favorite_num = {'andrii': '4', 'ann': '2', 'max': '18', 'leto': '1', 'david': '9'}
fav_num = favorite_num['andrii']
fav_num1 = favorite_num['ann']
fav_num2 = favorite_num['max']
fav_num3 = favorite_num['leto']
fav_num4 = favorite_num['david']

print(f"Andrii favorite num is {fav_num}.\nAnn favorite num is {fav_num1}."
      f"\nMax favorite num is {fav_num2}. \nLeto favorite num is {fav_num3}.\nDavid favorite num is {fav_num4}.")
print("00000000000000000000000000000000000")

for key, value in favorite_num.items():
      print(f"\nKey :{key.title()} {value}")

      #print(f"Num: {value}")
print("==============================")

#for name in sorted(favorite_num.keys()):
#      print(name.title())
print("===========================")

#for name in favorite_num:
#      print(name.upper())

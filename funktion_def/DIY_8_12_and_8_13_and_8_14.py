# def sndwich_list(*sendwiches):
#     for sendwich in sendwiches:
#         print(sendwich)
#
# sndwich_list('chees', 'salami')

"""
def build_profile(first, last, age, **user_info):

#     створити словник, що містить всю інформацію про користувача

    user_info['first_name'] = first
    user_info['last_name'] = last
    user_info['age'] = age
    return user_info
user_profilr = build_profile('andrii', 'yarovskiy', '42',
                             lokalizacion= 'ukraina',
                             field= 'python',
                             )
print(user_profilr)

"""
def make_car(car_barnd, car_model, **other_info):

    other_info['brand'] = car_barnd
    other_info['model'] = car_model
    print(other_info)
    return other_info
car = make_car('renault', 'logan' ,color= 'red',year='2007')
car = make_car('subaru', 'outback', color= 'blue', tow_package= 'True')


print('||||||||||||||||||||||||||||||||||||||||||||')

def make_car(**kwargs):



    return kwargs

car = make_car(marka='subaru', model='outback', color= 'blue', tow_package= 'True')
print(car)
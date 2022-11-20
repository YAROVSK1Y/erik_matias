
fruits = ['strawberries', 'cherry', 'grapes', 'pears', 'bananas']
favorite_fruits = ['strawberries', 'cherry', 'grapes']

if fruits in favorite_fruits:
    favorite = 'strawberries'
if 'cherry' in favorite_fruits:
    favorite = 'cherry'
if 'grapes' in favorite_fruits:
    favorite = 'grapes'
if 'pears' in favorite_fruits:
    favorite = 'pears'
if 'bananas' in favorite_fruits:
    favorite = 'bananas'

print(f"Your really like {favorite}!")




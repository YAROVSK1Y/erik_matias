
user_log = input('Please , sey your name ')

filename = 'user_logging.txt'
with open(filename, 'a') as file_objekt:
    file_objekt.write(f"{user_log.title()}\n")
print(user_log)
promt = "Why do you like programming?\n"
promt += "Enter 'quit' to end program.\n "

survey = ''
print(promt)
with open('survey.txt', 'w') as file_objekt:
      while survey != 'quit':
        survey = input()
        file_objekt.write(f"{survey}\n")



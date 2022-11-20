
#Почати з креслень які треба роздрукувати

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Симулювати друк кожного креслення
# Перенести кожен рисунок до completed_models після друку

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)


#Показати всі готові моделі

print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

############################################################



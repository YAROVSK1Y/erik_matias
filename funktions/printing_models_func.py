
def print_models(unprinted_designs, completed_models):
    """" Симулювати друк кожного креслення, доки всі не закінчаться.
         Перенести кожен рисунок до completed_models після друку.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
        

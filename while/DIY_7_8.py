"""--------------|7_8| Sandwiches |----------------"""
"""
sandwich_order = ['chees sandwich', 'tunafish sandwich', 'beef sandwich',
                  'nutella sandwich']
finished_sandwiches = []

while sandwich_order:
    ready_sandwiches = sandwich_order.pop()
    print(f"I made you {ready_sandwiches.title()}")
    finished_sandwiches.append(ready_sandwiches)
    
print(f"We prepared the following sandwiches -- \n{finished_sandwiches} ")
"""

""" -----------------|7-9| no pastroma |--------------"""

sandwich_order = ['chees sandwich',  'tunafish sandwich', 'beef sandwich', 'pastrami sandwich',
                  'nutella sandwich', 'pastrami sandwich']

print(f"with pastrami sandwich \n{sandwich_order}  ")

while 'pastrami sandwich' in sandwich_order:
    sandwich_order.remove('pastrami sandwich')

print(f"with out 'pastrami sandwich'\n{sandwich_order} ")

"""-------------------------|7-10|The perfect vacation|-----------"""
people = {}
name = input("What your name? ")
vacation = input("Where do you dream of going? ")


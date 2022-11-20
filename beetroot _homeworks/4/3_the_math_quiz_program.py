"""Task 3

The math quiz program.

Write a program that asks the answer for a mathematical expression,
checks whether the user is right or wrong,
and then responds with a message accordingly."""

question = input("Question:\n2+2=\n"
                 "What is the correct answer?")

expression = 4
if question.isdigit():
    question = int(question)
else:
    print("it's not numeric")

if question == expression:
    print("Yes")
else:
    print("No")

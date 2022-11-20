from survey import AnonymousSurvey
# Визначити запитання та створити опитування.
question = ("Яка твоя найбільша любов?")
my_survey = AnonymousSurvey(question)

# Показати запитання та зберігти відповіді на нього.

my_survey.show_question()
print("Enter 'q' to eny time to quit.\n")
while True:
    responce = input("Це - ")
    if responce == 'q':
        break
    my_survey.show_store_responsw(responce)
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()

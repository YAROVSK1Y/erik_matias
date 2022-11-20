
class AnonymousSurvey:
    """Зібрати анонімні відповіді на питання"""
    def __init__(self, question):
        """Зберегти питання та підготуватись до збереження відповідей."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Показати питання."""
        print(self.question)

    def store_response(self, new_response):
        """Зберігати одну відповідь на питання."""
        self.responses.append(new_response)

    def show_results(self):
        """Показати всі надані відповіді."""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")




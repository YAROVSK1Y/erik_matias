import unittest
from survey import AnonymousSurvey

class TestAnonymusSurvey(unittest.TestCase):
    """Тест для класу AnonimusSurvey."""

    def setUp(self):
        """
        Створити опитування та набір відповідей для вісх тестувальних відповідей.
        """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']


    def test_store_single_response(self):
        """Перевірити чи одиночна відповідь зберігається правільно."""
        # question = "What language did you first learn to speak?"
        # my_survey = AnonymousSurvey(question)
        # my_survey.store_response("English")
        # self.assertIn('English', my_survey.responses)
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """
        Перевірити, чи три індивідуальні відповіді зберігаються правитьно.
        """
        # question = "What language did you first learn to speak?"
        # my_survey = AnonymousSurvey(question)
        # responses = ['English', 'Spanish', 'Mandarin']
        # for response in responses:
        #     my_survey.store_response(response)
        #
        # for response in responses:
        #     self.assertIn(response, my_survey.responses)
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

if __name__ == '__main__':
    unittest.main()

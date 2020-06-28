import unittest
from AninimSurvey import *

class testAnonimSurvey(unittest.TestCase):
    """Тест для класса AS"""
    def setUp(self):
        """
        Создать данные для опроса
        :return:
        """
        question = "На каком языке вы хотите начать программировать?"
        self.my_survey = AnonimSurvey(question)
        self.responses = ["Java","Javascript","Python"]

    def store_single_responses(self):
        """проверяет был ли правильно у нас сохранен одиночный ответ"""
        self.my_survey.store_response(self.responses[0])
        # здесь мы описываем, входит ли у нас наш ответ в список возможных ответов
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """Проверяет что каждый отдельный ответ был сохранен правильно"""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response,self.my_survey.responses)

unittest.main()
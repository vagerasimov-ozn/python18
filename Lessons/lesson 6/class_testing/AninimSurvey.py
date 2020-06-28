class AnonimSurvey:
    """Собирает анонимные ответы на опросник"""

    def __init__(self,question):
        """Содержит вопрос, и подготавливает список для ответа"""
        self.question = question
        self.responses = []

    def show_question(self):
        """Показать вопрос"""
        print(self.question)

    def store_response(self, new_response):
        """Сохраняет у нас ответ"""
        self.responses.append(new_response)
    def show_results(self):
        print("результаты нашего опроса следующие:")
        for response in self.responses:
            print(f"- {response}")
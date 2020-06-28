from AninimSurvey import *


question = "Какой язык вы хотите изучать первым?"
my_survey = AnonimSurvey(question)

my_survey.show_question()
print("Введите q для окончания работы программы \n")
while True:
    response = input("Язык: \n")
    if response == 'q':
        break
    my_survey.store_response(response)

print("\n Спасибо за участие в этом опросе большое")
my_survey.show_results()
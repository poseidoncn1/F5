from survey import AnonymousSurney

# 定义一个问题，并创建一个表示调查的AnnomousSurvey对象
question =  "What language did you first learn to speak ?"
my_survey = AnonymousSurney(question)
# 显示问题
my_survey.show_question()
print("\nEnter q at any time to quit.\n")
while True:
    response = input("Language :")
    if response == 'q':
        break
    my_survey.store_reponse(response)
print("\nThank you to everyone who participated in this survey！")
my_survey.show_result()

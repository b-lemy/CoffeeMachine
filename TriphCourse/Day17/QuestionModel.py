from data import question_data


class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


question_bank = []
for question in question_data:
    question_text = question['text']
    question_answer = question['answer']

    new_question = Question(question_text, question_answer)

    question_bank.append(new_question)

print(question_bank)

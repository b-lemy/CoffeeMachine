from QuestionModel import question_bank


class QuizBrain:

    def __init__(self):
        self.question_number = 0
        self.question_list = question_bank


quiz_brain = QuizBrain()

print(quiz_brain.question_list)

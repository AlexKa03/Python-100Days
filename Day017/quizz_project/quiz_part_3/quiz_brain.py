class QuizzBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        user_choice = input(f"Q.{self.question_number}: {question.text} (True/False): ")

# DONE-1: Asking the questions
# TODO-2: Checking if we're at the end of the quiz
# TODO-3: Checking if the answer was correct
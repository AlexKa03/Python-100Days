class QuizzBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def check_answer(self, user_answer, true_answer, passed_questions):
        if user_answer.lower() == true_answer.lower():
            print("Correct!")
            self.score += 1
        else:
            print("Incorrect!")
        print(f"The answer was: {user_answer}")
        print(f"Your current score is: {self.score}/{passed_questions}\n")

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        user_choice = input(f"Q.{self.question_number}: {question.text} (True/False): ")
        self.check_answer(user_choice, question.answer, self.question_number)

# DONE-1: Asking the questions
# DONE-2: Checking if we're at the end of the quiz
# DONE-3: Checking if the answer was correct
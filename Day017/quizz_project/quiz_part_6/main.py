from question_model import Question
from data import question_data
from quiz_brain import QuizzBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizzBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print(f"You completed the Quiz\nYour final score was: {quiz.score}/{len(quiz.question_list)}")
from question_model import Qusetion
from new_data import New_data
from quiz_brain import QuizBrain
question_bank=[]
for question in New_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Qusetion(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
#print(quiz)
while quiz.still_has_question():
    quiz.next_question()

print("You have completed the Quiz")
print(f"Your final score {quiz.score}/{quiz.question_number}")
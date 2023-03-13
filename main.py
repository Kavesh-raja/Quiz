from question_model import Qusetion
from data import question_data
from quiz_brain import QuizBrain
question_bank=[]
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Qusetion(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
#print(quiz)
quiz.next_question()
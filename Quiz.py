from art import logo
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
print("Welcome to the Quiz")
print(logo)
question_bank = []
for i in range(0, len(question_data)):
    question_bank.append(Question(question_data[i]["question"], question_data[i]["correct_answer"]))

quiz = QuizBrain(question_bank)
quiz.next_question()
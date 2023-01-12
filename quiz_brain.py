from time import sleep


class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank
        self.score = 0

    def next_question(self):
        self.question_number += 1
        current_question = self.question_list[self.question_number - 1]
        print("Q" + str(self.question_number) + ". " + current_question.question)
        if self.question_number == len(self.question_list):
            print("All questions completed")
            print("Your final score is : " + str(self.score))
            sleep(10)
            exit(1)
        choice = input("True/False : ").lower()
        if choice == current_question.answer.lower():
            print("Correct Answer!")
            self.score += 1
            print("Your score is " + str(self.score) + "/" + str(self.question_number))
            print("\n\n")
            self.next_question()
        elif choice != "true" and choice != "false":
            print("Program Terminated! Wrong input")
            sleep(10)
        else:
            print("Wrong Answer")
            print("The current answer is : " + current_question.answer)
            print("Your score is " + str(self.score) + "/" + str(self.question_number))
            print("\n\n")
            self.next_question()

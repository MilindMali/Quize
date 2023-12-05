#todo: Asking the quetion to user
#todo: checking if the answer is correct
#todo: checking if we are the end of quiz

class QuizBrain:
    # following are attributes
    def __init__(self,q_list):
        self.question_number=0
        self.question_list=q_list
        self.score=0

    # following is method
    def still_have_questions(self):
        return self.question_number<len(self.question_list)

    # following are methods
    def next_question(self):
        current_question=self.question_list[self.question_number]
        self.question_number+=1
        user_answer=input(f"{self.question_number}. {current_question.text} (True/False) :")
        self.check_answer(user_answer,current_question.answer)

    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower()==correct_answer.lower():
            self.score+=1
            print("you got it right !")
        else:
            print("Thats Wrong answer")
        print(f"The correct answer is  {correct_answer}.")
        print(f"Your score is {self.score}/{self.question_number}")
        print("\n")


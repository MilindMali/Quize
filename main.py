from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
# challenge= we have to create list of quetion object, where question object will have the text and ans

question_bank=[]

for question in question_data:
    que_text = question["text"]
    que_ans = question["answer"]
    new_que=Question(que_text, que_ans)
    question_bank.append(new_que)

#print(question_bank[0].answer)

# now we have create question bank which list of question object

quiz=QuizBrain(question_bank)

while quiz.still_have_questions():
    quiz.next_question()

print("You have completed the quiz !")
print(f"Your final score is {quiz.score}/{len(question_bank)}")

from Question import Question 
question_prompt = [
    "What will you do if you find a wallet on the street? \n(a) Keep it \n(b) Hand it over to the police \n(c) Try to find the owner",
    "What bigger than yourself do you believe in? \n(a) God \n(b) Humanity \n(c) Science",
    "what is capitol of India? \n(a) Mumbai \n(b) New Delhi \n(c) Chennai"
]

questions = [
    Question(question_prompt[0], "b"),
    Question(question_prompt[1], "a"),
    Question(question_prompt[2], "b")
]

def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.text + "\n")
        if answer == question.answer:
            score += 1
    print("You got "+ str(score) + "/" + str(len(questions)) + " correct")
    return score
    
    

score = run_quiz(questions)
if score == 3:
    print("You are a great person")
elif score == 2:
    print("You are a good person")
elif score == 1:
    print("You are an average person")
else:
    print("You need to work on yourself you are Fukked up")

# Building a multiple choice quiz

question_pronpts = [  # this is an array
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color aree Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n"
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]


# So we create a question class because we need to keep track of some attributes. The questions prompt and the answer need to be kept track of

# Makes a new file called "Question.py"

# In "Question.py":

class Question:
    def __init__(self):  # so we want to describe the sort of attributes that would be involved in a question


# example:

class Question:
    def __init__(self, prompt, answer):  # take those values and assign them to the actual class object
        self.prompt = prompt  # object's prompt is equal to class's prompt
        self.answer = answer  # object's answer is equal to class's answer


# Think about patch bay in audio work. You have to connect them to tell them what is what


# Goes back to app.py:

from Question import Question

question_prompts = [  # This array simply runs the question
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color aree Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n"
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]
# creates another array

questions = [
    # This array is calling for questions from the other array. This array prompts the questions, and stores the correct answer which is checked by line 52
    Question(question_prompts[0], "a")  # index 0 which is line 33, the answer
    Question(question_prompts[1], "c")  # index 1 which is line 34, the answer
    Question(question_prompts[2], "b")  # index 2 which is line 35, the answer
]


# next we create the function that runs the test/quiz


def run_test(questions):
    score = 0  # score starts at 0
    for question in questions:  # for loop. For each question in the array questions on line 39. Also seen as for each question object inside of this questions array; I want do do something:
        answer = input(
            question.prompt)  # store user input in variable "answer". This is the variable which stores the input from "question.prompt" on lines 40-42
        if answer == question.answer:  # if line 51/user input answer is equal to answers in lines 23, 40-42
            score += 1  # add 1 to the score variable
    print("You got " + str(score) + "/" + str(
        len(questions)) + "correct")  # Prints the user score out of total number of questions


#                   convert score to str  long way of saying how many questions, converted to string

run
test(questions)  # runs the function run test on line 48 using the array "questions" on lines 39-43

# Runs the function which starts with a variable score of 0. Next is a for loop that says for each question(the objects) in questions(an array; line 40-42) [that calls another array to ask the questions,
# which it does by calling the array on lines 32-36 by index number(0-2), then it has the correct answer to those 2 otherwise unrerlated arrays.] if the users input answer matches the array's answer, add
# 1 point to variable score. Lastly print out the user score out of (/) the entire number of questions(which would be how many you could have had correct)
questions = ("Who developed Python Programming Language? :",
             "Which type of Programming does Python support? :",
             "Is Python case sensitive when dealing with identifiers? :",
             "Which of the following is the correct extension of the Python file? :",
             "Is Python code compiled or interpreted? :",
             "All keywords in Python are in _________ :",
             "Which of the following character is used to give single-line comments in Python? :",
             "Which keyword is used for function in Python language? :",
             "What arithmetic operators cannot be used with strings in Python? :")

options = (("A.Wick van Rossum","B.Rasmus Lerdorf","C.Guido van Rossum","D.Niene Stom"),
           ("A.object-oriented programming","B.structured programming","C.functional programming","D.all of the mentioned"),
           ("no","yes","machine dependent","none of the above"),
           ("A:.python","B:.pl","C:.p","D:.py"),
           ("A.It is both compiled and interpreted","B.It is neither compiled and interpreted","C.It is only compiled","D.It is only interpreted"),
           ("A.Capitalized","B.lower case","C.UPPER CASE","D.None of the mentioned"),
           ("A.//","B.#","C.!","D./*"),
           ("A.Function","B.def","C.Fun","D.Define"),
           ("A.*","B.-","C.+","D.All of the Above"))
answers = ("C","D","B","D","A","D","B","B","B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("----------------------")
print("       RESULTS        ")
print("----------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")
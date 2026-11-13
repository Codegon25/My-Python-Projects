#Python quiz game
 
questions = ("What is 47 + 68?: ",
             "Solve for x: 3x - 7 = 20: ",
             "What is 3/4 + 1/8?: ",
             "What is 15% of 240?: ",
             "A rectangle has a length of 12 cm and a width of 5 cm. What is its area?: ")

options = (("A. 105","B. 115","C. 125","D. 135"),
           ("A. x = 7","B. x = 8","C. x = 9","D. x = 10"),
           ("A. 4/12","B. 5/8","C. 7/8","D. 1"),
           ("A. 24","B. 30","C. 36","D. 40"),
           ("A. 17cm2","B. 34cm2","C. 60cm2","D. 65cm2"))

answers = ("B","C","C","C","C")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B,C ,D) ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT")
    else:
        print("INCORRECT")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("--------------------------")
print("          RESULTS         ")
print("--------------------------")

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
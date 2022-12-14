
"""Welcome message for quiz game asking for name and inserting it into said message"""

name = input("what is you name: ")


print("")
print("*" *80)
print(f"Welcome {name} to the Harry Potter sorting quiz. Answer these 7 questions")
print("honestly, and at the end of this quiz you will be sorted into your")
print("Hogwarts House where you will spend the next 7 years studying magic")
print("at the greatest school of Witchcraft and Wizardry. Best of luck!!")
print("")
print("*" *80)

def open_questions():
    quiz_questions = []

    with open("requirements.txt", "r") as f:
        
        questions = f.readlines()
        for quest in questions:
            quiz_questions.append(quest.strip())
    return quiz_questions

quiz_questions = open_questions()
for question in quiz_questions:
    print("Question1")
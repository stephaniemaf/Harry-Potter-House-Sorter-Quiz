"""
variables to store answers for questions to show which house user belongs too
"""



def welcome_message():
    """
    Welcome message for quiz game asking for name and inserting it
    into said message
    """

    name = input("what is you name: ")

    print("")
    print("*" * 80)
    print(f"Welcome {name} to the Harry Potter sorting quiz. Answer these 7 questions")
    print("honestly, and at the end of this quiz you will be sorted into your")
    print("Hogwarts House where you will spend the next 7yrs studying magic")
    print("at the greatest school of Witchcraft and Wizardry. Best of luck!!")
    print("")
    print("*" * 80)


def questions_for_quiz():

    """
    dictionary of questions to be presented to the user
    """
    gryffindor = 0
    hufflepuff = 0
    ravenclaw = 0
    slytherin = 0


    questions = [{"question": "How would you like to be known in history?",
                    "choices": ["The wise", "The good", "The bold", "The Great"
                    ]}]

    print(questions)

    guess = input("Please enter you answer: ")
    if guess == "a":
        ravenclaw += 1
    elif guess == "b":
        hufflepuff += 1
    elif guess == "c":
        gryffindor += 1
    elif guess == "d":
        slytherin += 1
    else:
        print("Unknown entry please try again")


welcome_message()
questions_for_quiz()

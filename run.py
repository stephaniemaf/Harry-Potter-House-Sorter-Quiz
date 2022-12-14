gryffindor = 0
hufflepuff = 0
ravenclaw = 0
slytherin = 0


def welcome_message():
    """
    Welcome message for quiz game asking for name and inserting it into said message
    """

    name = input("what is you name: ")


    print("")
    print("*" *80)
    print(f"Welcome {name} to the Harry Potter sorting quiz. Answer these 7 questions")
    print("honestly, and at the end of this quiz you will be sorted into your")
    print("Hogwarts House where you will spend the next 7 years studying magic")
    print("at the greatest school of Witchcraft and Wizardry. Best of luck!!")
    print("")
    print("*" *80)



def questions_for_quiz():
    questions = [{"question":"How would you like to be known in history?",
     "choices":["The wise", "The good", "The bold", "The Great"
                ]}]

    print(questions)


welcome_message()
questions_for_quiz()


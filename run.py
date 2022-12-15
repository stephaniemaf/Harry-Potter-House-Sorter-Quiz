"""
variables for storing user answers
"""

GRYFFINDOR = 0
HUFFLEPUFF = 0
RAVENCLAW = 0
SLYTHERIN = 0


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


def questions_for_quiz(GRYFFINDOR, RAVENCLAW, HUFFLEPUFF, SLYTHERIN):

    """
    variables to store answers for questions to show which house user belongs
    too, and underneath this is a list of dictionaries to store the questions
    """

    questions = [{
                    "question": "How would you like to be known in history?",
                    "choices": ["a) The wise", "b) The good", "c) The bold",
                    "d) The Great"
                ]},
                {
                    "question": "Which Quality best describes you?",
                    "choices": ["a) Brave","b) Intelligent","c) Ambitious",
                    "d) Empathetic"
                ]},
                {
                    "question": "Which potion would you rather have?",
                    "choices": ["a) Glory", "b) Wisdom", "c) Love", "d) Power",
                ]},
                {
                    "question": "You're trapped in a burning building.What do you do?",
                    "choices": ["a) Run and Grab your friend thats also trapped",
                    "b) Save yourself, of course!!", 
                    "c) Give it a shot but your not sure you can save your friend",
                    "d) It depends if you can save your friend you will, if not...your just gonna run."]
                }]
              
    for question in questions:
        print(question["question"])
        print("")
        print("Choices:")
        for i in question["choices"]:
            print(i)

        guess = input("Please enter you answer: ")
        if guess == "a":
            RAVENCLAW += 1
        elif guess == "b":
            HUFFLEPUFF += 1
        elif guess == "c":
            GRYFFINDOR += 1
        elif guess == "d":
            SLYTHERIN += 1
        else:
            print("Unknown entry please try again")


def sort_into_house():
    """
    conditional statement to sort user into house
    """

    if GRYFFINDOR > RAVENCLAW and GRYFFINDOR > HUFFLEPUFF and GRYFFINDOR > SLYTHERIN:
        print("you in gryffindor")
    elif RAVENCLAW > GRYFFINDOR and RAVENCLAW > HUFFLEPUFF and RAVENCLAW > SLYTHERIN:
        print("you are in Ravenclaw")
    elif HUFFLEPUFF > GRYFFINDOR and HUFFLEPUFF > RAVENCLAW and HUFFLEPUFF > SLYTHERIN:
        print("you are in hufflepuff")
    elif SLYTHERIN > GRYFFINDOR and SLYTHERIN > RAVENCLAW and SLYTHERIN > HUFFLEPUFF:
        print("you are in slytherin")
    else:
        print("hmm you dont seem to be in any house you can pick your own ")


welcome_message()
questions_for_quiz(GRYFFINDOR, RAVENCLAW, HUFFLEPUFF, SLYTHERIN)
sort_into_house()

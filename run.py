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
                    "b) Save yourself, of course!!", "c) Give it a shot but your not sure you can save your friend",
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

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

    input("Are you ready press enter to begin...")


def questions_for_quiz():

    """
    variables to store answers for questions to show which house user belongs
    too, and underneath this is a list of dictionaries to store the questions
    """
    global RAVENCLAW, GRYFFINDOR, HUFFLEPUFF, SLYTHERIN
    questions = [{
                    "question": "How would you like to be known in history?",
                    "choices": [("a) The wise",RAVENCLAW), "b) The good", "c) The bold",
                    "d) The Great"
                ]},
                {
                    "question": "Which Quality best describes you?",
                    "choices": [("a) Brave",GRYFFINDOR),"b) Intelligent","c) Ambitious",
                    "d) Empathetic"
                ]},
                {
                    "question": "Which potion would you rather have?",
                    "choices": [("a) Glory",HUFFLEPUFF), "b) Wisdom", "c) Love", "d) Power",
                ]},
                {
                    "question": "You're trapped in a burning building.What do you do?",
                    "choices": [("a) Run and Grab your friend thats also trapped",RAVENCLAW),
                    "b) Save yourself, of course!!", 
                    "c) Give it a shot but your not sure you can save your friend",
                    "d) It depends if you can save your friend you will, if not...your just gonna run."]
                }]
    
    for question in questions:
        print(question["question"])
        print("")
        print("Choices:")
        for i in question["choices"]:
            print(i[0])
        
        guess = input("Please enter you answer: ")
        if guess == "a":
            question["choices"][0][1] += 1
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
    print(RAVENCLAW)
    if GRYFFINDOR > max(HUFFLEPUFF, RAVENCLAW, SLYTHERIN):
        print("you have been sorted into gryffindor")
    elif RAVENCLAW > max(HUFFLEPUFF, GRYFFINDOR, SLYTHERIN):
        print("you have been sorted into Ravenclaw")
    elif HUFFLEPUFF > max(GRYFFINDOR, RAVENCLAW, SLYTHERIN):
        print("you have been sorted into hufflepuff")
    elif SLYTHERIN > max(GRYFFINDOR, RAVENCLAW, SLYTHERIN):
        print("you have been sorted into slytherin")
    else:
        print("hmm you dont seem to be in any house you can pick your own ")



def main():
    """
    run all programme fumctions
    """
    welcome_message()
    questions_for_quiz()
    sort_into_house()


main()

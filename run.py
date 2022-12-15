"""
variables for storing user answers
"""

HOUSES = {
 "GRYFFINDOR": 0,
 "HUFFLEPUFF": 0,
 "RAVENCLAW": 0,
 "SLYTHERIN": 0,
}

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
    global HOUSES
    questions = [{
                    "question": "How would you like to be known in history?",
                    "choices": [
                        ("a) The wise", "RAVENCLAW"),
                        ("b) The good", "GRYFFINDOR"),
                        ("c) The bold", "HUFFLEPUFF"),
                        ("d) The Great", "SLYTHERIN"),
                    ]
                },
                {
                    "question": "Which Quality best describes you?",
                    "choices": [
                        ("a) Brave", "GRYFFINDOR"),
                        ("b) Intelligent", "RAVENCLAW"),
                        ("c) Ambitious", "SLYTHERIN"),
                        ("d) Empathetic", "HUFFLEPUFF"),
                    ]
                },
                {
                    "question": "Which potion would you rather have?",
                    "choices": [
                        ("a) Glory", "GRYFFINDOR"), 
                        ("b) Wisdom", "RAVENCLAW"), 
                        ("c) Love", "HUFFLEPUFF"),
                        ("d) Power", "SLYTHERIN"),
                    ]
                },
                {
                    "question": "You're trapped in a burning"
                    + "building.What do you do?",
                    "choices": [
                        ("a) Run and Grab your friend whos trapped too", "GRYFFINDOR"),
                        ("b) Save yourself, of course!!", "SLYTHERIN"),
                        ("c) Give it a shot but your not sure you can save your friend", "HUFFLEPUFF"),
                        ("d) It depends if you can save your friend you will,"
                         + "if not...your just gonna run.", "RAVENCLAW"),
                    ]
                }]
    
    question_num = 0

    while (question_num < len(questions)):
        question = questions[question_num]
        print(question["question"])
        print()
        print("Choices:")
        for i in question["choices"]:
            print(i[0])
        
        guess = input("Please enter you answer: ")
        house = ""
        if guess == "a":
            house = question["choices"][0][1]
            question_num += 1
            HOUSES[house] += 1
        elif guess == "b":
            house = question["choices"][1][1]
            question_num += 1
            HOUSES[house] += 1
        elif guess == "c":
            house = question["choices"][2][1]
            question_num += 1
            HOUSES[house] += 1
        elif guess == "d":
            house = question["choices"][3][1]
            question_num += 1
            HOUSES[house] += 1
        else:
            print("Unknown entry please try again")


def sort_into_house():
    """
    conditional statement to sort user into house
    """
    max_one = max(HOUSES["HUFFLEPUFF"], HOUSES["RAVENCLAW"], HOUSES["SLYTHERIN"])
    max_two = max(HOUSES["HUFFLEPUFF"], HOUSES["GRYFFINDOR"], HOUSES["SLYTHERIN"])
    max_three = max(HOUSES["GRYFFINDOR"], HOUSES["RAVENCLAW"], HOUSES["SLYTHERIN"])
    max_four = max(HOUSES["HUFFLEPUFF"], HOUSES["RAVENCLAW"], HOUSES["GRYFFINDOR"])
    if HOUSES["GRYFFINDOR"] > max_one:
        print("you have been sorted into gryffindor")
    elif HOUSES["RAVENCLAW"] > max_two:
        print("you have been sorted into Ravenclaw")
    elif HOUSES["HUFFLEPUFF"] > max_three:
        print("you have been sorted into hufflepuff")
    elif HOUSES["SLYTHERIN"] > max_four:
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

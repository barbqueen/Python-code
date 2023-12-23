#File: exercise_9.py
#Description: 
#Assignment Number: chapter10-9
#Kevin Liu
#Github<barbqueen>

class Question:
    def __init__(self, question, options, correct_answer):
        self.__question = question
        self.__options = options
        self.__correct_answer = correct_answer

    def get_question(self):
        return self.__question

    def get_options(self):
        return self.__options

    def get_correct_answer(self):
        return self.__correct_answer

def play_trivia(questions):
    player1_score = 0
    player2_score = 0

    for i in range(len(questions)):
        print("\nQuestion", i + 1)
        print(questions[i].get_question())
        options = questions[i].get_options()
        for j in range(len(options)):
            print(f"{j + 1}. {options[j]}")

        while True:
            try:
                player1_answer = int(input("Player 1, enter your answer (1-4): "))
                if 1 <= player1_answer <= 4:
                    break
                else:
                    print("Invalid input. Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        while True:
            try:
                player2_answer = int(input("Player 2, enter your answer (1-4): "))
                if 1 <= player2_answer <= 4:
                    break
                else:
                    print("Invalid input. Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        if player1_answer == questions[i].get_correct_answer():
            player1_score += 1
        if player2_answer == questions[i].get_correct_answer():
            player2_score += 1

    print("\nGame Over! Results:")
    print("Player 1 Score:", player1_score)
    print("Player 2 Score:", player2_score)
    if player1_score > player2_score:
        print("Player 1 wins!")
    elif player2_score > player1_score:
        print("Player 2 wins!")
    else:
        print("It's a tie!")


question1 = Question("What is the capital of France?", ["London", "Paris", "Berlin", "Rome"], 2)
question2 = Question("Which planet is known as the Red Planet?", ["Mars", "Venus", "Jupiter", "Saturn"], 1)
question3 = Question("Which is fastest?", ["Car", "Plane", "Rocket", "Bike"],3 )
question4 = Question("What is the capital of Germany?", ["Berlin", "Paris", "London", "Kanzas"], 1)
question5 = Question("What is the derivative of sin(X)?", ["cosh(x)", "tan(x)", "cos(x)", "sec(x)"], 3)
questions_list = [question1, question2, question3, question4, question5]

play_trivia(questions_list)

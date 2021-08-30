"""
Simulates a magic eight ball.
Prompts the user to type a yes or no question and gives
a random answer from a set of prefabricated responses.
"""
import random

# Assign a number to each output
ANSWER_1 = "YES."
ANSWER_2 = "DEFINITELY"
ANSWER_3 = "Maybe."
ANSWER_4 = "NEVERRRRR!"
ANSWER_5 = "Not sure."
ANSWER_6 = "NOT POSSIBLE!"
ANSWER_7 = "Yeah Nah Maybe"

def main():
    # Fill this function out!
    # randomly choose a number
    while True:
        question = input("Ask a yes or no question: ")
        answer_number = random.randint(1,7)
        # correlate the answer to the numbers
        if answer_number == 1:
            print(ANSWER_1)
        if answer_number == 2:
            print(ANSWER_2)
        if answer_number == 3:
            print(ANSWER_3)
        if answer_number == 4:
            print(ANSWER_4)
        if answer_number == 5:
            print(ANSWER_5)
        if answer_number == 6:
            print(ANSWER_6)
        if answer_number == 7:
            print(ANSWER_7)

if __name__ == "__main__":
    main()

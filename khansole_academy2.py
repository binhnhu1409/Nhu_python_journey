"""
Randomly generate addition problems until 
user has gotten 3 problems correct in a row.
"""
import random

CORRECT_ANSWER = 3

def main():
    correct_number = 0
    while correct_number < CORRECT_ANSWER:
        num1 = random.randint(10,99)
        num2 = random.randint(10,99)
        print("What is "+str(num1)+" + "+str(num2)+"?")
        user_num = int(input("Your answer: "))
        if user_num != num1 + num2:
            correct_number = 0
            print("Incorrect. The expected answer is "+str(num1+num2))
        else:
            correct_number += 1
            print("Correct! You've gotten "+str(correct_number)+" in a row.")
    print("Congratulations! You mastered addition.")


if __name__ == '__main__':
    main()

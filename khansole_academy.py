"""
Prints out a randomly generated addition problem
and checks if the user answers correctly.
"""

import random 

def main():
    num1 = random.randint(10,99)
    num2 = random.randint(10,99)
    print("What is "+str(num1)+" + "+str(num2)+"?")
    user_num = int(input("Your answer: "))
    if user_num == num1 + num2:
        print("Correct!")
    else:
        print("Incorrect. The expected answer is "+str(num1+num2))


if __name__ == '__main__':
    main()

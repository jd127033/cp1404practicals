"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random

def main():
    score = float(input("Enter score: "))
    result = check_score(score)
    print(result)
    random_score = random.randint(0, 100)
    random_result = check_score(random_score)
    print(f"The result from your random number {random_score} is {random_result}.")

""" Checks score and determines result """
def check_score(score):
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result

main()




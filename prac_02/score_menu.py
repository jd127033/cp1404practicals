""" Score menu program - menu for many functionalities using user input """

MENU = """(G)et a valid score (must be 0 - 100 inclusive)
    (P)rint result
    (S)how stars
    (Q)uit"""

def main():
    score = int(input("Score: "))
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score(score)
        elif choice == "P":
            result = check_score(score)
            print(result)
        elif choice == "S":
            print_asterisks(score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Goodbye.")

""" Allow user to update score if invalid """
def get_valid_score(score):
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Score: "))
    return score

""" Checks if the score is good bad or excellent """
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

""" Prints a number of stars equal to the inputted score """
def print_asterisks(score):
    print("*" * score)

main()



